import asyncio
from azure.ai.textanalytics.aio import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
import os
import random


#Updated Version of Language API with enhanced features like parallel requests, error handling and all API-Services etc.

async def safe_langAPIrequest(client, serviceType, text):

    SERVICE_MAP = {
        "sent": lambda client, text: client.analyze_sentiment([text]),
        "keyp": lambda client, text: client.extract_key_phrases([text]),
        "lang": lambda client, text: client.detect_language([text]),
        "naer": lambda client, text: client.recognize_entities([text]),
        "rpii": lambda client, text: client.recognize_pii_entities([text]),
        #"summ": lambda client, text: client.begin_extract_summary([text]),
    }

    LRO_MAP = {
        "rphi": lambda client, text: client.begin_analyze_healthcare_entities([text]),
        "summ": lambda client, text: client.begin_extract_summary([text]),
    }

    for attempt in range(5):
        try:
            # Normal Services
            if serviceType in SERVICE_MAP:
                coro = SERVICE_MAP[serviceType](client, text)
                result = await coro
                return result[0]

            # Long-running Services
            elif serviceType in LRO_MAP:
                poller = await LRO_MAP[serviceType](client, text)
                result = await poller.result()
                async for page in result:
                    docs = page.get("results", [])
                    if docs:
                        return docs[0]

            else:
                raise ValueError(f"[-] Unknown service type: {serviceType}")

        except HttpResponseError as e:
            if e.status_code == 429:
                wait = (2 ** attempt) + random.random()
                print(f"[-] [429] Retry in {wait:.2f}s")
                await asyncio.sleep(wait)
            else:
                print(f"Error: {e}")
                return None

async def main():
    try:
        endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
        key = os.environ["AZURE_LANGUAGE_KEY"]
    except KeyError:
        print("[-] Missing environment variable 'AZURE_CUSTOM_VISION_ENDPOINT' or 'AZURE_CUSTOM_VISION_KEY'")
        print("[-] Set them before running this sample.")
        exit()
    
    docs = [
        "Microsoft Azure, sometimes stylized Azure, and formerly Windows Azure, is the cloud computing platform developed by Microsoft. It offers management, access and development of applications and services to individuals, companies, and governments through its global infrastructure. It also provides capabilities that are usually not included within other cloud platforms, including software as a service (SaaS), platform as a service (PaaS), and infrastructure as a service (IaaS). Microsoft Azure supports many programming languages, tools, and frameworks, including Microsoft-specific and third-party software and systems. Azure was first introduced at the Professional Developers Conference (PDC) in October 2008 under the codename \"Project Red Dog\". It was officially launched as Windows Azure in February 2010 and later renamed to Microsoft Azure on March 25, 2014. Max Mustermann likes this Project very much!",
        "Patient needs to take 50 mg of ibuprofen, and 2 mg of Coumadin."
    ]

    serviceType = "summ"

    async with TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        disable_service_logs=True
    ) as client:

        tasks = [safe_langAPIrequest(client, serviceType, d) for d in docs]
        results = await asyncio.gather(*tasks)

        for text, r in zip(docs, results):

            OUTPUT_MAP = {
                "sent": lambda r: f"[+] Sentiment Analysis -> {r.sentiment}",
                "keyp": lambda r: f"[+] Key-Phrase Analysis -> {r.key_phrases}",
                "lang": lambda r: f"[+] Language Detection -> {r.primary_language.name} ({r.primary_language.iso6391_name})",
                "naer": lambda r: f"[+] Entities recognized -> {'; '.join([e.text for e in r.entities])}",
                "rpii": lambda r: f"[+] PII recognized -> {'; '.join([e.text for e in r.entities])}",
                "rphi": lambda r: f"[+] PHI recognized -> {'; '.join([e.text for e in r.entities])}",
                "summ": lambda r: f"[+] Summary -> {" ".join([sentence.text for sentence in r.sentences])}"
            }

            print("RESULT:",r)
            if r:
                formatter = OUTPUT_MAP.get(serviceType)
                if formatter:
                    print(formatter(r))
                else:
                    print(f"[!] Unknown service type: {serviceType}")
            else:
                print(f"[-] {text} -> Error")

asyncio.run(main())
