from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
import os
import random

#Updated Version of Language API for Long-running Services with enhanced features like parallel requests, error handling and all API-Services etc.

def safe_langAPIrequest(client, serviceType, text):

    LRO_MAP = {
        "rphi": lambda client, text: client.begin_analyze_healthcare_entities([text]),
        "summ": lambda client, text: client.begin_extract_summary([text]),
    }

    for attempt in range(5):
        try:
            if serviceType in LRO_MAP:
                poller = LRO_MAP[serviceType](client, text)
                result = poller.result()
                return result
            else:
                raise ValueError(f"[-] Unknown service type: {serviceType}")

        except HttpResponseError as e:
            if e.status_code == 429:
                wait = (2 ** attempt) + random.random()
                print(f"[-] [429] Retry in {wait:.2f}s")
            else:
                print(f"Error: {e}")
                return None

if __name__ == "__main__":

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

    client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        disable_service_logs=True
    )
    
    results = [safe_langAPIrequest(client, serviceType, d) for d in docs]

    for text, r in zip(docs, results):

        OUTPUT_MAP = {
            "rphi": lambda r: f"[+] PHI recognized -> {"; ".join([entity.text for entity in result.entities])}",
            "summ": lambda r: f"[+] Summary -> {" ".join([sentence.text for sentence in result.sentences])}"
        }

        for result in r:    
            if r:
                formatter = OUTPUT_MAP.get(serviceType)
                if formatter:
                    print(formatter(r))
                else:
                    print(f"[!] Unknown service type: {serviceType}")
            else:
                print(f"[-] {text} -> Error")