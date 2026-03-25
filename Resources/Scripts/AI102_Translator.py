from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

# AI-102 Prep - Azure AI Translator Text SDK Example

def translateText(text,lang):
    load_dotenv()

    try:
        key = os.getenv("AZURE_TRANSLATION_KEY")
        region = os.getenv("AZURE_TRANSLATION_REGION")
        endpoint = os.getenv("AZURE_TRANSLATION_TEXT_ENDPOINT")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        exit()
    
    try:
        credential = AzureKeyCredential(key)
        client = TextTranslationClient(credential=credential,region=region)

        response = client.translate(body=[text],to_language=[lang],from_language="en")

        return response[0]["translations"][0]["text"]
    
    except Exception as e:
        print("[-] Translation error:",e)
        return False


def getSupportedLanguages(printit=False):
    load_dotenv()
    listofLanguages = []

    try:
        key = os.getenv("AZURE_TRANSLATION_KEY")
        region = os.getenv("AZURE_TRANSLATION_REGION")
        endpoint = os.getenv("AZURE_TRANSLATION_TEXT_ENDPOINT")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        exit()
    try:
        credential = AzureKeyCredential(key)
        client = TextTranslationClient(credential=credential,region=region)
        response = client.get_supported_languages()

        if response.translation is not None:
            if printit:
                print("[+] Translation Languages:")

            for key, value in response.translation.items():
                listofLanguages.append(key)
                if printit:
                    print(f"{key} - {value.name} ({value.native_name})")

        if printit == False:
            return listofLanguages

    except HttpResponseError as exception:
        if exception.error is not None:
            print(f"[+] Error Code: {exception.error.code}")
            print(f"[+] Message: {exception.error.message}")
        return False


if __name__ == "__main__":

    #text = input("[!] Input a text to translate: ")
    #lang = input("[!] Enter the target language (i.e. 'de'): ")
    #print(translateText(text,lang))

    print(getSupportedLanguages())
