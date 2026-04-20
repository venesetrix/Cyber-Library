from AI102_KeyVaultHelper import getKey
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import os

#WARNING!!! Code won't work in 04/2026 because AutoGen is not migrated to Responses API yet

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

def agent():
    
    setup = getAzureSetup()
    if not setup:
        raise RuntimeError("[-] Azure setup couldn't be initialized.")

    endpoint, key, apiversion, deployment = setup

    solver = AssistantAgent(
        name="Solver",
        llm_config={
            "api_type": "azure",
            "model": deployment,
            "api_key": key,
            "base_url": endpoint,
            "api_version": apiversion,
            "temperature": 0,
            "max_tokens": 800
        }

    )

    operator = UserProxyAgent(
        name="Operator",
        human_input_mode="NEVER",
        code_execution_config=False
    )

    operator.initiate_chat(
        solver,
        message="Plan a 2-day wedding anniversary in Augsburg, Bavaria for 2 persons."
    )

if __name__ == "__main__":
    agent()