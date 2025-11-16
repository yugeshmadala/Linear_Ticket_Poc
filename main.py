from gmail_reader import read_unread_emails
from groq_classifier import classify_task
from linear_client import create_ticket

def run():
    print("🔎 Checking for unread emails...\n")
    emails = read_unread_emails()

    if not emails:
        print("📭 No unread emails found.")
        return 
    
    for email in emails:
        text = email["subject"] + "\n" + email["body"]
        print(f"Email: {email['subject']}")

        if classify_task(text):
            print(" Task detected! Creating Linear ticket...")
            result = create_ticket(email["subject"], email["body"])
            print(" Ticket created:", result)
        else:
            print("Not a task. Skipping.")

        print("-" * 40)

if __name__ == "__main__":
    run()

    