from azure.ai.textanalytics.aio import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import asyncio
import os

async def main():
    try:
        endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
        key = os.environ["AZURE_LANGUAGE_KEY"]
    except KeyError:
        print("[-] Missing environment variable 'AZURE_CUSTOM_VISION_ENDPOINT' or 'AZURE_CUSTOM_VISION_KEY'")
        print("[-] Set them before running this sample.")
        exit()

    async with TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        disable_service_logs=True
    ) as client:

        docs = ["Woodgrove Bank's new mobile app is slow, but the support staff is excellent."]
        sentiment_result = (await client.analyze_sentiment(docs))[0]
        key_phrases_result = (await client.extract_key_phrases(docs))[0]

        print("Sentiment: ", sentiment_result.sentiment)
        print("Key phrases:", key_phrases_result.key_phrases)

asyncio.run(main())
