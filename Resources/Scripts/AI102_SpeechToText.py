import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

# AI-102 Prep - Azure AI Speech-to-Text SDK Example

load_dotenv()

try:
    key = os.getenv("AZURE_STT_KEY")
    endpoint = os.getenv("AZURE_STT_ENDPOINT")
    region = os.getenv("AZURE_REGION")
    filepath = os.getenv("AZURE_STT_AUDIO_PATH")
except KeyError:
    print("[-] Missing environment variable")
    print("[-] Set them before running this sample.")
    exit()


speech_config = speechsdk.SpeechConfig(
    subscription=key,
    region=region
)

audio_config = speechsdk.audio.AudioConfig(
    filename=filepath
)

try:
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("[+] Speech-to-text Result: ", result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print(f"[-] No speech recognized: {result.no_match_details}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"[-] canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("[-] Error details: {}".format(cancellation_details.error_details))
except Exception as e:
    print("[-] Error with file or configuration.")