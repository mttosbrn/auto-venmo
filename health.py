from datetime import datetime
from utils import get_env, verify_env_vars, env_vars, get_env_vars, Venmo
from dotenv import load_dotenv

def main(now):
  load_dotenv()
  date = now.strftime("%B %d, %Y")
  time = now.strftime("%H:%M%p")
  print(f'🕘 Monthly health check running on {date} at {time}.\n')

  print("🔍 Verifying environment variables...")
  numOfExpected =  2
  envVarsAreDefined = verify_env_vars(env_vars, numOfExpected)

  if envVarsAreDefined:
    print(f'✅ Found all {numOfExpected} environment variables.\n')
  else:
    print('❌ Failed to verify environment variables.\n')

  access_token, *tail = get_env_vars(env_vars)

  venmo = Venmo(access_token)

  print("🤑 Verifying Venmo client is working...")
  userId = venmo.get_user_id_by_username("Jordan-Mishlove")

  if userId:
    print('✅ Venmo client is working as expected.\n')
  else:
    print('❌ Failed to get userId using Venmo client.\n')

  returnedUserId = bool(userId)

  if envVarsAreDefined and returnedUserId:
    print('✅ Everything looks good in the health check')
  elif envVarsAreDefined:
    print('❌ Venmo client might not be working. 1/2 checks failed in health script.')
  elif returnedUserId:
    print('❌ Envrionment variables check did not pass. 1/2 checks failed in health script.')
  else:
    print('❌ Venmo client and environment variables did not pass. 2/2 checks failed in health script.')

# Grab current date and passing in when running function
now = datetime.now()
main(now)