from AI102_KeyVaultHelper import getKey
from openai import AzureOpenAI
from datetime import date
from dotenv import load_dotenv
import argparse, os, sys, base64

# AI-102 Prep - Azure OpenAI Service Example

# Helper function to get the endpoint and API-Key for the requests
def getAzureSetup(serviceType):

    load_dotenv()
   
    try:
        if serviceType == "txt":
            apiversion = os.getenv("AZURE_OPENAI_TEXT_APIVERSION")
            endpoint = os.getenv("AZURE_OPENAI_TEXT_ENDPOINT")
            keyVaultName = os.getenv("AZURE_KEYVAULT_NAME")
            keyName = os.getenv("AZURE_OPENAI_TEXT_KEYNAME")
            deployment = os.getenv("AZURE_OPENAI_TEXT_DEPLOYMENTNAME")
        elif serviceType == "img":
            apiversion = os.getenv("AZURE_OPENAI_IMAGE_APIVERSION")
            endpoint = os.getenv("AZURE_OPENAI_IMAGE_ENDPOINT")
            keyVaultName = os.getenv("AZURE_KEYVAULT_NAME")
            keyName = os.getenv("AZURE_OPENAI_IMAGE_KEYNAME")
            deployment = os.getenv("AZURE_OPENAI_IMAGE_DEPLOYMENTNAME")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        return False
    
    try:
        key = getKey(keyVaultName=keyVaultName,keyName=keyName)
    except Exception as e:
        print("[-] Error loading key from KeyVault.", e)
        return False
    
    return endpoint, key, apiversion, deployment

def createImage(prompt:str):

    endpoint, key, apiversion, deployment = getAzureSetup("img")

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=key,
        api_version=apiversion
    )

    try:
        response = client.images.generate(
            model=deployment,
            prompt=prompt,
            size="1024x1024",
            quality="high",
            n=1
        )
    except Exception as e:
        print("[-] Error while generating the image.", e)
        return False

    image_base64 = response.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    imgName = f"{date.today().isoformat()}-openAI-Image.png"

    with open(imgName, "wb") as f:
        f.write(image_bytes)

    print(f"[+] Image saved as {imgName}")


def createTxt(prompt:str):
    
    endpoint, key, apiversion, deployment = getAzureSetup("txt")

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=key,
        api_version=apiversion
    )

    sys.stdout.flush()

    try:
        response = client.responses.create(
            stream=True,
            input=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_output_tokens=16384,
            model=deployment
        )
        
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="")
            elif event.type == "response.completed":
                break
    except Exception as e:
        print("[-] Error while generating the answer.", e)
        return False

    client.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Send a prompt to text or image generation OpenAI Service"
    )

    parser.add_argument("--prompt", help="Prompt for generation")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--img", action="store_true", help="Option: Text from file")
    group.add_argument("--txt", action="store_true", help="Option: Text from ID card")

    args = parser.parse_args()

    if args.img:
        createImage(args.prompt)
    elif args.txt:
        createTxt(args.prompt)
