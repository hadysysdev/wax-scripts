import os
from pyeoskit import  wallet
from dotenv import load_dotenv
load_dotenv()

#import your account private key here
wallet.import_key(os.getenv('WALLET_NAME'), os.getenv('WALLET_KEY'))