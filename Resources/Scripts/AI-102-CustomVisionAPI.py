import os
from pprint import pprint
import requests

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
try:
    endpoint = os.environ["AZURE_CUSTOM_VISION_ENDPOINT"]
    key = os.environ["AZURE_CUSTOM_VISION_KEY"]
except KeyError:
    print("[-] Missing environment variable 'AZURE_CUSTOM_VISION_ENDPOINT' or 'AZURE_CUSTOM_VISION_KEY'")
    print("[-] Set them before running this sample.")
    exit()

# Request headers.
headers = {
    'Content-Type': 'application/octet-stream',
    'Prediction-Key': key
}

image_path = "C:\\Users\\benjamin.stemmler\\Downloads\\sample\\test_image.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()

# Call the API.
try:
    response = requests.post(endpoint, headers=headers, data=image_data)
    response.raise_for_status()
    analysis = response.json()

    print("\n[+] Response:\n")
    for count in range(len(analysis["predictions"])):
        print("Prediction #", count+1, ":")
        for prediction in analysis["predictions"]:
            if prediction["tagName"] == analysis["predictions"][count]["tagName"]:
                print(prediction["tagName"], "-", int(prediction["probability"]*100),"%\n")
    #image_caption = analysis["description"]["captions"][0]["text"].capitalize()
except Exception as ex:
    raise ex