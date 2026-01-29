# Mimecast API Toolkit

A collection of Python scripts to interact with the Mimecast API 2.0. This toolkit provides utilities for authentication, account support information, email queue monitoring, dashboard notifications, account information, and URL decoding. More on the way.

## Features

- **Centralized Authentication:** OAuth2 token management handled automatically.
- **Get Support Info:** Retrieve account support details.
- **Email Queues:** Monitor inbound and outbound email queues for the last 24 hours.
- **Dashboard Notifications:** Fetch dashboard notifications for a specific account.
- **Get Account Info:** Retrieve detailed account information.
- **URL Decode:** Decode Mimecast rewritten URLs (TTP).
- **More on the way.**

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
    Create a `credentials.txt` file in the project root with your Mimecast API Client ID and Secret initially:
    ```text
    client_id=YOUR_CLIENT_ID
    client_secret=YOUR_CLIENT_SECRET
    ```
    Once configured, you can run `python3 get_account.py` to find your `account_code` in the output. Then, add it to your `credentials.txt`:
    ```text
    client_id=YOUR_CLIENT_ID
    client_secret=YOUR_CLIENT_SECRET
    account_code=YOUR_ACCOUNT_CODE
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

### 3. Get Dashboard Notifications
Fetches dashboard notifications for the configured account code.
```bash
python3 get_dashboard_notifications.py
```

### 4. Get Account Info
Fetches detailed information about the Mimecast account.
```bash
python3 get_account.py
```

### 5. Decode URL
Decodes a Mimecast rewritten URL. You can provide the URL as an argument or interactively.
```bash
# Argument
python3 decode_url.py "https://url.us.m.mimecastprotect.com/..."

# Interactive
python3 decode_url.py
```
