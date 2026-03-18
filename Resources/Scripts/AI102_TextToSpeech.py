import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

# AI-102 Prep - Azure AI Text-to-Speech SDK Example

def main():
    load_dotenv()

    try:
        key = os.getenv("AZURE_STT_KEY")
        region = os.getenv("AZURE_REGION")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        exit()

    speech_config = speechsdk.SpeechConfig(
        subscription=key,
        region=region
    )

    speech_config.speech_synthesis_voice_name = "fr-FR-DeniseNeural"

    try:
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        result = speech_synthesizer.speak_text("Bonjour, bienveneu chez Paris.")

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("[+] Speech synthesized!: ", result.text)
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"[-] canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("[-] Error details: {}".format(cancellation_details.error_details))
    except Exception as e:
        print("[-] Error with file or configuration.",e)

if __name__ == "__main__":
    main()