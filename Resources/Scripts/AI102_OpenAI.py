from AI102_KeyVaultHelper import getKey
from openai import AzureOpenAI
from dotenv import load_dotenv
import argparse, os

# AI-102 Prep - Azure OpenAI Service Example

# Helper function to get the endpoint and API-Key for the requests
def getAzureSetup():

    load_dotenv()
   
    try:
        apiversion = os.getenv("AZURE_OPENAI_TEXT_APIVERSION")
        endpoint = os.getenv("AZURE_OPENAI_TEXT_ENDPOINT")
        keyVaultName = os.getenv("AZURE_KEYVAULT_NAME")
        keyName = os.getenv("AZURE_OPENAI_TEXT_KEYNAME")
        deployment = os.getenv("AZURE_OPENAI_TEXT_DEPLOYMENTNAME")
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

    endpoint, key, apiversion = getAzureSetup()

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=key,
        api_version=apiversion
    )

    response = client.images.generate(
        mode="dalle3",
        prompt=prompt,
        size="1024x1024",
        response_format="url",
        output_format="jpg",
        quality="standard",
        n=1
    )

    print("[+] Image URL:", response["data"][0]["url"])

def createTxt(prompt:str):
    
    endpoint, key, apiversion, deployment = getAzureSetup()

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=key,
        api_version=apiversion
    )

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
        print("[-] Sorry...but this service is temporarily not available!")
        #createImage(args.prompt)
    elif args.txt:
        createTxt(args.prompt)
