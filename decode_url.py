import requests
import json
import sys
import auth

BASE_URL = "https://api.services.mimecast.com"

def decode_url(token, url_to_decode):
    """Decodes a single Mimecast URL."""
    print(f"Decoding URL: {url_to_decode}")
    api_url = f"{BASE_URL}/api/ttp/url/decode-url"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"data": [{"url": url_to_decode}]}
    
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error decoding URL: {e}")
        return None

if __name__ == "__main__":
    url_to_decode = None
    
    if len(sys.argv) > 1:
        url_to_decode = sys.argv[1]
    else:
        try:
            url_to_decode = input("Enter Mimecast URL to decode: ").strip()
        except EOFError:
            pass

    if not url_to_decode:
        print("Usage: python3 decode_url.py <MIMECAST_URL>")
        print("Example: python3 decode_url.py https://protection.mimecast.com/...")
        sys.exit(1)
    
    token = auth.get_token()
    result = decode_url(token, url_to_decode)
    
    if result:
        print("\n--- Decode Results ---")
        for item in result.get("data", []):
            if item.get("success"):
                print(f"Original URL: {item.get('url')}")
            else:
                print(f"Failed to decode: {item}")
