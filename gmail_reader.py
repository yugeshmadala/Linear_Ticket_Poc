import base64
import os
import re
from email.message import EmailMessage

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_gmail_service():
    creds = None 
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def read_unread_emails():
    service = get_gmail_service()
    results = service.users().messages().list(userId="me", q="is:unread").execute()
    messages = results.get("messages", [])

    emails = []

    if not messages:
        return emails
    
    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        headers = msg_data["payload"]["headers"]
        subject = next(
            (h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)"
        )

        parts = msg_data["payload"].get("parts", [])
        body = ""

        if parts:
            for part in parts:
                if part["mimeType"] == "text/plain":
                    data = part["body"]["data"]
                    body = base64.urlsafe_b64decode(data).decode("utf-8")
                    break 
        emails.append({"id": msg["id"], "subject": subject, "body": body})

    return emails

