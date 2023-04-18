from venmo_api import Client
from dotenv import load_dotenv
from datetime import datetime

from utils import get_env, env_vars, get_week, Venmo

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, k_friend_id = actualVars

  week = get_week(now)
  venmo = Venmo(access_token)

  friends =[
    {
      "name": "Billy",
      "id": k_friend_id,
    },
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = "Payment for week " + week + " -Matt"
    amount = 20.00
    success = venmo.request_money(id, amount, description)
    if success:
      successfulRequests.append(success)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
