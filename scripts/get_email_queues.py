import requests
import json
from datetime import datetime, timedelta, timezone
import auth

BASE_URL = "https://api.services.mimecast.com"

def get_queues(token):
    """Fetches Email Queues for the last 24 hours."""
    print("Fetching Email Queues...")
    api_url = f"{BASE_URL}/api/email/get-email-queues"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    now = datetime.now(timezone.utc)
    start = now - timedelta(hours=24)
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    
    payload = {
        "data": [{
            "start": start.strftime(fmt),
            "end": now.strftime(fmt)
        }]
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching queues: {e}")
        return None

if __name__ == "__main__":
    token = auth.get_token()
    queues = get_queues(token)
    
    if queues:
        print("\n--- Queue Results ---")
        data = queues.get("data", [])
        if not data:
            print("No data returned.")
        
        for item in data:
            if "fail" in item:
                 print(f"Error: {item.get('fail')}")
                 continue
                 
            print("-" * 30)
            inbound = item.get("inboundEmailQueue", [])
            outbound = item.get("outboundEmailQueue", [])
            
            print(f"Inbound Queue Items: {len(inbound)}")
            for q in inbound:
                print(f"  {q.get('date')}: {q.get('count')}")
                
            print(f"\nOutbound Queue Items: {len(outbound)}")
            for q in outbound:
                print(f"  {q.get('date')}: {q.get('count')}")
            print("-" * 30)
