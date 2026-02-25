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

# Load image to analyze into a 'bytes' object
try:
    with open("sample.py", "rb") as f:
        loadedImage = f.read()
except KeyError:
    print("[-] Couldn't open file.")
    exit()

# Get a caption for the image. This will be a synchronously (blocking) call.
result = client.analyze(
    image_data=loadedImage,
    visual_features=[VisualFeatures.READ],
)
print("[+] Results received!\n")
print("[+] Image analysis results:")
if result.read is not None:
    for line in result.read.blocks[0].lines:
        print(f"   Line: '{line.text}'")
print()