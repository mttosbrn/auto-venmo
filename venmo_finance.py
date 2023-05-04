#%%

from venmo_api import Client
from dotenv import load_dotenv
from datetime import datetime

from utils import get_env, env_vars, Venmo

load_dotenv()  # take environment variables from .env
actualVars = []
for var in env_vars:
    actualVars.append(get_env(var))

access_token, b_friend_id, c_friend_id, c2_friend_id, l_friend_id = actualVars

client = Client(access_token=access_token)

def callback(transactions_list):
    for transaction in transactions_list:
        print(transaction)

# callback is optional. Max number of transactions per request is 50.
client.user.get_user_transactions(user_id=c_friend_id,
                                     callback=callback)

#%%

import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt
from collections import namedtuple

# c_friend loan characteristics
original_balance = 9703.36
coupon = 0.045
term = 24

# payments
periods = range(1, term+1)
interest_payment = npf.ipmt(
    rate=coupon / 12, per=periods, nper=term, pv=-original_balance)
principal_payment = npf.ppmt(
    rate=coupon / 12, per=periods, nper=term, pv=-original_balance)

plt.stackplot(periods, interest_payment, principal_payment, 
              labels=['Interest', 'Principal'])
plt.legend(loc='upper left')
plt.xlabel("Period")
plt.ylabel("Payment")
plt.margins(0, 0)

# pandas float formatting_
pd.options.display.float_format = '{:,.2f}'.format

# cash flow table_
cf_data = {'Interest': interest_payment, 'Principal': principal_payment}
cf_table = pd.DataFrame(data=cf_data, index=periods)
cf_table['Payment'] = cf_table['Interest'] + cf_table['Principal']
cf_table['Ending Balance'] = original_balance - \
                             cf_table['Principal'].cumsum()
cf_table['Beginning Balance'] = [original_balance] + \
                                list(cf_table['Ending Balance'])[:-1]
cf_table = cf_table[['Beginning Balance', 'Payment', 'Interest', 
                     'Principal', 'Ending Balance']]
cf_table.head(8)

#%%