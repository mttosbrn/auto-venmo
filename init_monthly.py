from venmo_api import Client
from dotenv import load_dotenv
from datetime import datetime

from utils import get_env, env_vars, get_month, Venmo

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, b_friend_id, c_friend_id, c2_friend_id, l_friend_id = actualVars

  month = get_month(now)
  venmo = Venmo(access_token)

  amy_monthly =[
    {
      "name": "Casey",
      "id": c2_friend_id,
    },
     {
      "name": "Logan",
      "id": l_friend_id,
    },
  ]

  matt_monthly =[
    {
      "name": "Caio",
      "id": c_friend_id,
    },
  ]

  successfulRequests = []
  expectedRequests = len(amy_monthly) + len(matt_monthly)

# "Payment for " + month + "

  for friend in amy_monthly:
    name = friend["name"]
    id = friend["id"]
    description = "This is just a test, thanks -Amy's assitant 🤵🏻"
    amount = 1.00
    success = venmo.request_money(id, amount, description)
    if success:
      successfulRequests.append(success)

  for friend in matt_monthly:
    name = friend["name"]
    id = friend["id"]
    description = "Payment for " + month + ", thanks -Matt"
    amount = 423.53
    success = venmo.request_money(id, amount, description)
    if success:
      successfulRequests.append(success)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
