from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions
from azure.core.credentials import AzureKeyCredential
import os

client = ContentSafetyClient(
    os.environ["AZURE_CONTENT_SAFETY_ENDPOINT"], 
    AzureKeyCredential(os.environ["AZURE_CONTENT_SAFETY_KEY"])
)

result = client.analyze_text(AnalyzeTextOptions(text="I love you so much!"))

for item in result.categories_analysis:
    print(item.category, item.severity)
    if item.severity >= 4:
        print("Na na na, you unkind person!")
    elif item.severity == 2:
        print("Okay, that's not that nice!")
    else:
        print("Oh, how nice. Thank you!")