import os
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# AI-102 Prep - Azure AI QuestionAnswering Example
# NOT TESTED!

load_dotenv()

try:
    endp = os.getenv("AZURE_LANGUAGE_ENDPOINT")
    key = os.getenv("AZURE_LANGUAGE_KEY")
except KeyError:
    print("[-] Missing environment variable")
    print("[-] Set them before running this sample.")
    exit()

client = QuestionAnsweringClient(
    endpoint=endp,
    credential=AzureKeyCredential(key)
)

# Ask a question
response = client.get_answers(
    question="Who is Mickey Mouse?",
    project_name="",
    deployment_name="production"
)

# Print top answer
if response.answers:
    print("Top answer:", response.answers[0].answer)
else:
    print("I really don't know!")

