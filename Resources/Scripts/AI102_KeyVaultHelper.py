import os
import argparse
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

# AI-102 Prep - KeyVaultHelper

def getKey(keyName,keyVaultName=""):
    
    if not keyVaultName:
        load_dotenv()
        keyVaultName = os.environ["AZURE_KEYVAULT_NAME"]

    try:
        return SecretClient(vault_url=f"https://{keyVaultName}.vault.azure.net", credential=DefaultAzureCredential()).get_secret(keyName).value
    except Exception as e:
        print("[-] Error: ",e)
        return False

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Get a secret from Azure KeyVault"
    )
    parser.add_argument("keyName", help="Name of the Secret")
    parser.add_argument("--keyVault", help="Name of the KeyVault")

    args = parser.parse_args()

    print(getKey(args.keyName,args.keyVault))


    
