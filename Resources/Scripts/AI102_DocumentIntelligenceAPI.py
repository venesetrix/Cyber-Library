from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient, DocumentIntelligenceAdministrationClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeOutputOption, AnalyzeResult
from AI102_KeyVaultHelper import getKey
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
import re
import sys
import argparse
import base64
import numpy as np

# AI-102 Prep - Azure Document Intelligence SDK Example

# Input a path to or an URL of a file (i.e. a PDF) and extract it's text 
def getTextfromFile(filepath, detailed=False):
    
    endpoint, key = getDocIntelSetup()

    try:
        docIntelClient = DocumentIntelligenceClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )

        if is_url(filepath):
            poller = docIntelClient.begin_analyze_document(
                "prebuilt-read", AnalyzeDocumentRequest(url_source=filepath)
            )
        else:
            with open(filepath, "rb") as f:
                data = f.read()
            
            encodedFile = base64.b64encode(data).decode("utf-8")
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

# Input a path to or an URL of a file (i.e. a PDF) and extract it's text 
def getFiguresFromFile(filepath):
    
    endpoint, key = getDocIntelSetup()

    docIntelClient = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    with open(filepath, "rb") as f:
        poller = docIntelClient.begin_analyze_document(
            "prebuilt-layout",
            body=f,
            output=[AnalyzeOutputOption.FIGURES],
        )

    result: AnalyzeResult = poller.result()
    operation_id = poller.details["operation_id"]

    if result.figures:
        for figure in result.figures:
            if figure.id:
                response = docIntelClient.get_analyze_result_figure(
                    model_id=result.model_id, result_id=operation_id, figure_id=figure.id
                )
                with open(f"{figure.id}.png", "wb") as writer:
                    writer.writelines(response)
    else:
        print("[-] No figures found.")

# Input a file (i.e. an image) of an ID card and extract the information based on a prebuilt model
def getTextfromID(filepath):

    endpoint, key = getDocIntelSetup()

    docIntelClient = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    if is_url(filepath):
            poller = docIntelClient.begin_analyze_document(
                "prebuilt-idDocument", AnalyzeDocumentRequest(url_source=filepath)
            )
    else:
        with open(filepath, "rb") as f:
            data = f.read()
            
        encodedFile = base64.b64encode(data).decode("utf-8")
        poller = docIntelClient.begin_analyze_document(
            "prebuilt-idDocument", AnalyzeDocumentRequest(bytes_source=encodedFile)
        )

    IDs: AnalyzeResult = poller.result()

    if IDs.documents:
        for idx, id in enumerate(IDs.documents):
            print(f"[+] --------Analysis of ID #{idx + 1}--------")
            print(f"[+] ID type: {id.doc_type if id.doc_type else 'N/A'}")
            if id.fields:
                print(f"[+] Document Number: {id.fields['DocumentNumber']['content']}")
                print(f"[+] Name: {id.fields['DateOfBirth']['content']}")
                print(f"[+] Date of birth: {id.fields['DateOfBirth']['content']}")
                print(f"[+] Date of Expiration: {id.fields['DateOfExpiration']['content']}")
                print(f"[+] Name: {id.fields['FirstName']['content']} {id.fields['LastName']['content']}")

# Input a file and extract checklists and their status
def getChecklistsfromFile(filepath):

    endpoint, key = getDocIntelSetup()

    docIntelClient  = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    if is_url(filepath):
            poller = docIntelClient.begin_analyze_document(
                "prebuilt-layout", AnalyzeDocumentRequest(url_source=filepath)
            )
    else:
        with open(filepath, "rb") as f:
            data = f.read()
            
        encodedFile = base64.b64encode(data).decode("utf-8")
        poller = docIntelClient.begin_analyze_document(
            "prebuilt-layout", AnalyzeDocumentRequest(bytes_source=encodedFile)
        )

    result = poller.result()

    for idx, style in enumerate(result.styles):
        print(
            "[+] Document contains {} content!".format(
            "handwritten" if style.is_handwritten else "no handwritten"
            )
        )
    
    # Regex: Find sections, starting with :unselected: or :selected:
    pattern = r"(?=(:(?:unselected|selected):))"

    for paragraph in result.paragraphs:
        parts = re.split(pattern, paragraph['content'])
        result = []

        i = 1
        while i < len(parts):
            tag = parts[i]
            content = parts[i+1].split(" :unselected:")[0].split(" :selected:")[0].strip()
            content = content.replace(":unselected:","[ ]")
            content = content.replace(":selected:", "[x]")
            result.append(f"{content}")
            i += 2

        for r in result:
            print(r)

# Get a list of the prebuilt models available
def getModels():

    endpoint, key = getDocIntelSetup()

    docIntelAdminClient = DocumentIntelligenceAdministrationClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    # Alle Modelle abrufen
    models = docIntelAdminClient.list_models()

    print("[+] Document Models:")
    for model in models:
        print(f"[+] ID: {model.model_id} | Description: {model.description}")

# Helper function to identify if the filepath is local or a URL
def is_url(s: str) -> bool:
    try:
        result = urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Helper function to print out a detailed analysis of a file
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

# Helper function to format bounding boxes for better output
def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    reshaped_bounding_box = np.array(bounding_box).reshape(-1, 2)
    return ", ".join(["[{}, {}]".format(x, y) for x, y in reshaped_bounding_box])

# Helper function to get the endpoint and API-Key for the requests
def getDocIntelSetup():

    load_dotenv()
   
    try:
        endpoint = os.getenv("AZURE_DOCINTEL_ENDPOINT")
        keyVaultName = os.getenv("AZURE_KEYVAULT_NAME")
        keyName = os.getenv("AZURE_DOCINTEL_KEYNAME")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        return False
    
    try:
        key = getKey(keyVaultName=keyVaultName,keyName=keyName)
    except Exception as e:
        print("[-] Error loading Admin-Key from KeyVault.", e)
        return False
    
    return endpoint, key

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Analyze a document"
    )

    parser.add_argument("--filepath", help="Path of a file to analyze")
    parser.add_argument("--detailed", action="store_true", help="Prints out a detailed analysis of the file")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--tff", action="store_true", help="Option: Text from file")
    group.add_argument("--tfi", action="store_true", help="Option: Text from ID card")
    group.add_argument("--cff", action="store_true", help="Option: Checklists from file")
    group.add_argument("--mod", action="store_true", help="Option: Get list of prebuilt models")

    args = parser.parse_args()

    # Case 1: --mod → no filepath
    if args.mod:
        if args.filepath:
            print("[-] Warning: --filepath for --mod is ignored.")
        if args.detailed:
            print("[-] Error: --detailed not used with --mod.")
            sys.exit(1)
        getModels()
        sys.exit(0)

    # Case 2: Filepath is necessary
    if not args.filepath:
        print("[-] Error: --filepath is not usable in this mode.")
        sys.exit(1)

    # Case 3: --detailed only with --tff option set
    if args.detailed and not args.tff:
        print("[-] Error: --detailed only used in --tff mode.")
        sys.exit(1)

    if args.tff:
        getTextfromFile(args.filepath, args.detailed)

    elif args.tfi:
        getTextfromID(args.filepath)

    elif args.cff:
        getChecklistsfromFile(args.filepath)

    else:
        print("[-] No option selected.")
