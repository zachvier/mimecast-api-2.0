import requests
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(SCRIPT_DIR, "credentials.txt")
BASE_URL = "https://api.services.mimecast.com"

def get_credentials():
    """Reads client_id and client_secret from a text file."""
    creds = {}
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    creds[key.strip().lower()] = value.strip()
    except FileNotFoundError:
        print(f"Error: {CREDENTIALS_FILE} not found.")
        sys.exit(1)
    
    return creds.get("client_id"), creds.get("client_secret")

def get_token():
    """Obtains the Bearer token using credentials from file."""
    client_id, client_secret = get_credentials()
    
    if not client_id or not client_secret or "YOUR_" in client_id:
        print(f"Please fill in your API credentials in {CREDENTIALS_FILE}")
        sys.exit(1)

    print("Authenticating...")
    url = f"{BASE_URL}/oauth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining token: {e}")
        if e.response is not None:
            print(f"Response: {e.response.text}")
        sys.exit(1)
