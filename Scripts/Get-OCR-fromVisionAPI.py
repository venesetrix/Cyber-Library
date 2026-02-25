import os
import sys
import argparse
from urllib.parse import urlparse

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def is_url(value: str) -> bool:
    """Return True if value looks like an http(s) URL."""
    try:
        u = urlparse(value)
        return u.scheme in ("http", "https") and bool(u.netloc)
    except Exception:
        return False

def get_env(name: str) -> str:
    """Fail-fast if env var is missing."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable '{name}'")
    return value

def create_client() -> ImageAnalysisClient:
    endpoint = get_env("AZURE_VISION_ENDPOINT")
    key = get_env("AZURE_VISION_KEY")
    return ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def analyze_local_file(client: ImageAnalysisClient, path: str):
    with open(path, "rb") as f:
        image_bytes = f.read()

    return client.analyze(
        image_data=image_bytes,
        visual_features=[VisualFeatures.READ],
    )

def analyze_remote_url(client: ImageAnalysisClient, url: str):
    # Für URL-Analysen gibt es analyze_from_url
    return client.analyze_from_url(
        image_url=url,
        visual_features=[VisualFeatures.READ],
    )

def print_read_result(result):
    print("[+] Image analysis results:")
    if getattr(result, "read", None) and result.read.blocks:
        for block in result.read.blocks:
            for line in block.lines:
                print(f"   Line: '{line.text}'")
    else:
        print("[-] (No READ/OCR results found)")

def main():
    parser = argparse.ArgumentParser(
        description="Analyze a local image file or a public image URL using Azure AI Vision Image Analysis."
    )
    parser.add_argument(
        "source",
        help="Local file path (e.g., ./image.jpg) or public URL (https://...)"
    )
    args = parser.parse_args()

    try:
        client = create_client()
        print("[+] Vision Client created!")

        if is_url(args.source):
            result = analyze_remote_url(client, args.source)
        else:
            result = analyze_local_file(client, args.source)

        print("[+] Results received!\n")
        print_read_result(result)

    except FileNotFoundError:
        print(f"[-] Couldn't open file: {args.source}", file=sys.stderr)
        sys.exit(2)
    except PermissionError:
        print(f"[-] No permission to read file: {args.source}", file=sys.stderr)
        sys.exit(2)
    except RuntimeError as e:
        print(f"[-] {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"[-] Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()