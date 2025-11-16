import os
import requests
from dotenv import load_dotenv

load_dotenv()

LINEAR_API_KEY = os.getenv("LINEAR_API_KEY")
TEAM_KEY = os.getenv("LINEAR_TEAM_KEY")

API_URL = "https://api.linear.app/graphql"

def create_ticket(title: str, description: str):
    """Create a Linear issue."""
    query = """
    mutation IssueCreate($input: IssueCreateInput!) {
      issueCreate(input: $input) {
        success
        issue {
          id
          url
        }
      }
    }
    """

    variables = {
        "input": {
            "teamId": TEAM_KEY,
            "title": title,
            "description": description
        }
    }

    headers = {
    "Authorization": LINEAR_API_KEY,
    "Content-Type": "application/json"
    }

    response = requests.post(
        API_URL,
        json={"query": query, "variables": variables,},
        headers=headers,
    )

    if response.status_code != 200:
        print(f"Linear API error {response.status_code}: {response.text}")
        return None

    try:
        data = response.json()
    except Exception as e:
        print(f"Failed to parse Linear API response: {e}")
        return None

    # Check for GraphQL errors
    if "errors" in data:
        print(f"Linear GraphQL errors: {data['errors']}")
        return None

    return data.get("data", {}).get("issueCreate", {})



