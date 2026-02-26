import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
try:
    endpoint = os.environ["AZURE_VISION_ENDPOINT"]
    key = os.environ["AZURE_VISION_KEY"]
except KeyError:
    print("[-] Missing environment variable 'AZURE_VISION_ENDPOINT' or 'AZURE_VISION_KEY'")
    print("[-] Set them before running this sample.")
    exit()

# Create an Image Analysis client for synchronous operations,
# using API key authentication
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)
print("[+] Vision Client created!")

# Get a caption for the image. This will be a synchronously (blocking) call.
result = client.analyze_from_url(
    image_url="https://aka.ms/azsdk/image-analysis/sample.jpg",
    visual_features=[
        VisualFeatures.CAPTION, 
        VisualFeatures.READ, 
        VisualFeatures.DENSE_CAPTIONS, 
        VisualFeatures.OBJECTS, 
        VisualFeatures.PEOPLE, 
        VisualFeatures.TAGS
        ],
    gender_neutral_caption=True,  # Optional (default is False)
    language="en"  # Optional (default is English; is not available for all features)
)
print("[+] Results received!\n")
print("[+] Image analysis results:")

# Print caption results to the console
print("[+]  Caption:")
if result.caption is not None:
    print(f"   Confidence {int(result.caption.confidence*100)}% - '{result.caption.text}'")
print()

# Print Dense Captions
print("[+] Dense Captions:")
if result.dense_captions is not None:
    for caption in result.dense_captions.list:
        print(f"   Confidence {int(caption.confidence*100)}% - '{caption.text}'")
print()

# Print Objects
print("[+] Objects:")
if result.objects is not None:
    for object in result.objects.list:
        print(f"   Confidence {int(object.tags[0].confidence*100)}% - '{object.tags[0].name}'")
print()

# Print text (OCR) analysis results to the console
print("[+] OCR-Read:")
if result.read is not None:
    for line in result.read.blocks[0].lines:
        print(f"   Line: '{line.text}'")
print()

# Print People analysis
print("[+] People:")
if result.people is not None:
    for person in result.people.list:
        print(f"   Confidence {int(person.confidence*100)}% - There are people in {person.bounding_box}")
print()

# Tag analysis
print("[+] Tags:")
if result.tags is not None:
    for tag in result.tags.list:
        print(f"   Confidence {int(tag.confidence*100)}% - '{tag.name}'")
print()