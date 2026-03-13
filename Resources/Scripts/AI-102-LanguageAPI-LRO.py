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
            






"""
def sample_extractive_summarization():
    # [START extract_summary]
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    document = [
        "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, "
        "human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI Cognitive "
        "Services, I have been working with a team of amazing scientists and engineers to turn this quest into a "
        "reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of "
        "human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the "
        "intersection of all three, there's magic-what we call XYZ-code as illustrated in Figure 1-a joint "
        "representation to create more powerful AI that can speak, hear, see, and understand humans better. "
        "We believe XYZ-code will enable us to fulfill our long-term vision: cross-domain transfer learning, "
        "spanning modalities and languages. The goal is to have pretrained models that can jointly learn "
        "representations to support a broad range of downstream AI tasks, much in the way humans do today. "
        "Over the past five years, we have achieved human performance on benchmarks in conversational speech "
        "recognition, machine translation, conversational question answering, machine reading comprehension, "
        "and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious "
        "aspiration to produce a leap in AI capabilities, achieving multisensory and multilingual learning that "
        "is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational "
        "component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
    ]

    poller = text_analytics_client.begin_extract_summary(document)
    extract_summary_results = poller.result()
    for result in extract_summary_results:
        if result.kind == "ExtractiveSummarization":
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in result.sentences]))
            )
        elif result.is_error is True:
            print("...Is an error with code '{}' and message '{}'".format(
                result.error.code, result.error.message
            ))
    # [END extract_summary]


if __name__ == "__main__":
    sample_extractive_summarization()
"""