# Linear_Ticket_Poc
This project is a Proof of Concept (POC) for automatically creating Linear tickets from Gmail emails using Groq LLM for task classification.

Features:
    1.Connects to Gmail and reads unread emails.
    2.Uses Groq LLM to classify if an email contains an ML-related task.
    3.Automatically creates a Linear ticket if a task is detected.
    4.Designed for local execution with Python and a virtual environment.

Setup:
1.Clone the repository:
2.Create and activate a virtual environment
3.Install dependencies
4.Create a .env file with the following variables:GROQ_API_KEY,LINEAR_API_KEY,LINEAR_TEAM_KEY
5.Make sure credentials.json for Gmail API is in the project folder.

Usage:
python main.py

1.The script checks for unread emails, classifies them, and creates Linear tickets automatically.
2.To demo, send an email with an ML-related task to the Gmail account used in the POC.
  
