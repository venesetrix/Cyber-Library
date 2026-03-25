from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from AI102_KeyVaultHelper import getKey
import os
import argparse
import base64
import numpy as np
from dotenv import load_dotenv

# AI-102 Prep - Azure Document Intelligence Example

def docIntel(filepath, detailed=False):
    load_dotenv()

    with open(filepath, "rb") as f:
        data = f.read()
    
    encodedFile = base64.b64encode(data).decode("utf-8")
    
    try:
        endpoint = os.getenv("AZURE_DOCINTEL_ENDPOINT")
        keyVaultName = os.getenv("AZURE_KEYVAULT_NAME")
        keyName = os.getenv("AZURE_DOCINTEL_KEYNAME")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        exit()
    
    try:
        key = getKey(keyVaultName=keyVaultName,keyName=keyName)
    except Exception as e:
        print("[-] Error loading Admin-Key from KeyVault.", e)
        return False

    try:
        docIntelClient = DocumentIntelligenceClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )

        poller = docIntelClient.begin_analyze_document(
            "prebuilt-read", AnalyzeDocumentRequest(bytes_source=encodedFile)
        )

        result = poller.result()

        print ("[+] Document contains content: \n\n", result.content)

        if detailed:
            detailedAnalysis(result)

    except Exception as e:
        print("[-] Error creating Document Intelligence Client.", e)
        return False


def detailedAnalysis(result):
    for idx, style in enumerate(result.styles):
        print("[+] Document contains {} content".format(
                    "handwritten" if style.is_handwritten else "no handwritten"
            )
        )

    for page in result.pages:
        print("[+] ----Analyzing page #{}----".format(page.page_number))
        print("[+] Page has width: {} and height: {}, measured with unit: {}".format(page.width, page.height, page.unit))

        print("\n[+] ----Line analysis----")
        for line_idx, line in enumerate(page.lines):
            print("[+] P{}-Line #{} has text content '{}' within bounding box '{}'".format(
                    page.page_number,
                    line_idx,
                    line.content,
                    format_bounding_box(line.polygon),
                )
            )

        print("\n[+] ----Word analysis----")
        for word in page.words:
            print("[+] Word '{}' has a confidence of {}".format(word.content, word.confidence))

        print("[+] ----End of page #{}----\n".format(page.page_number))

def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    reshaped_bounding_box = np.array(bounding_box).reshape(-1, 2)
    return ", ".join(["[{}, {}]".format(x, y) for x, y in reshaped_bounding_box])


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Analyze a document"
    )
    parser.add_argument("filepath", help="Path of a file to analyze")
    parser.add_argument("--detailed", action="store_true", help="Prints out a detailed analysis of the file")

    args = parser.parse_args()

    if args.detailed:
        docIntel(args.filepath, True)
    else:
        docIntel(args.filepath)
