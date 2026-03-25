from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, SearchableField
from AI102_KeyVaultHelper import getKey
import os
from dotenv import load_dotenv

# AI-102 Prep - Azure AI Search Example
# NOT FULLY TESTED!

def createSearchIndex(indexName,fields):
    load_dotenv()

    try:
        endpoint = os.getenv("AZURE_AISEARCH_ENDPOINT")
        keyVaultName = os.getenv("AZURE_KEYVAULT_NAME")
        keyName = os.getenv("AZURE_AISEARCH_ADMINKEY_NAME")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        exit()
    
    try:
        admin_key = getKey(keyVaultName=keyVaultName,keyName=keyName)
    except Exception as e:
        print("[-] Error loading Admin-Key from KeyVault.")
        return False
    
    try:     
        credential = AzureKeyCredential(admin_key)
        client = SearchIndexClient(endpoint=endpoint, credential=credential)

        try:
            client.create_index(SearchIndex(indexName, fields))
            print("[+] Index successfully created!")
        except Exception as e:
            print("[-] Could not create index: ",e)
            return False

    except Exception as e:
        print("[-] Index-Creation error:",e)
        return False

if __name__ == "__main__":

    #Example usage:
    name = "products"
    fields = [
        SimpleField(name="product_id", type="Edm.String", key=True),
        SearchableField(name="product_name", type="Edm.String", sortable=True),
        SearchableField(name="description", type="Edm.String")
    ]

    createSearchIndex(name, fields)
