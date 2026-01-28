# Mimecast API Toolkit

A collection of Python scripts to interact with the Mimecast API 2.0. This toolkit provides utilities for authentication, account support information, email queue monitoring, and URL decoding.

## Features

- **Centralized Authentication:** OAuth2 token management handled automatically.
- **Get Support Info:** Retrieve account support details.
- **Email Queues:** Monitor inbound and outbound email queues for the last 24 hours.
- **URL Decode:** Decode Mimecast rewritten URLs (TTP).

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/zachvier/mimecast-api-2.0.git
    cd mimecast-api-2.0
    ```

2.  Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

3.  Configure Credentials:
    Create a `credentials.txt` file in the project root with your Mimecast API Client ID and Secret:
    ```text
    client_id=YOUR_CLIENT_ID
    client_secret=YOUR_CLIENT_SECRET
    ```
    *Note: `credentials.txt` is git-ignored for security.*

## Usage

### 1. Get Account Support Info
Fetches support information for your Mimecast account.
```bash
python3 get_support_info.py
```

### 2. Get Email Queues
Fetches inbound and outbound email queue status for the last 24 hours.
```bash
python3 get_email_queues.py
```

### 3. Decode URL
Decodes a Mimecast rewritten URL. You can provide the URL as an argument or interactively.
```bash
# Argument
python3 decode_url.py "https://protection.mimecast.com/..."

# Interactive
python3 decode_url.py
```
