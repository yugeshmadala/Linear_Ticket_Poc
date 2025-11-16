import os
import requests
from dotenv import load_dotenv

load_dotenv()

LINEAR_API_KEY = os.getenv("LINEAR_API_KEY")
API_URL = "https://api.linear.app/graphql"

query = """
query {
  teams {
    nodes {
      id
      name
      key
    }
  }
}
"""

response = requests.post(
    API_URL,
    json={"query": query},
    headers={"Authorization": LINEAR_API_KEY},
)

print(response.json())
