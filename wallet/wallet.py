# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
from web3 import Web3
#from web3.auto.infura.kovan import w3
from eth_account import Account
import os
from bit import PrivateKeyTestnet #BTC test network create transaction
from bit.network import NetworkAPI #BTC API to send signed transaction

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic", "butter wine stamp blade three shift remind dutch marble december beauty foam")

# Import constants.py and necessary functions from bit and web3
from constants import *


# Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive, format=json):
    eth_command = '~/./derive -g --mnemonic="butter wine stamp blade three shift remind dutch marble december beauty foam" --cols=path,address,privkey,pubkey --format=json --coin=eth'

    btc_command = '~/./derive -g --mnemonic="butter wine stamp blade    three shift remind dutch marble december beauty foam" --cols=path,address,privkey,pubkey --format=json --coin=btc'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
#coins = {output,err}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
     if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
     if coin == BTC:
        return PrivateKeyTestnet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, recipient, amount):
    if coin == ETH:
         gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
         )
         return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
        "chainID": w3.net.chainId
         }
    elif coin == BTC:
         return PrivateKeyTestnet.prepare_transaction(account.address, [to, amount, BTC])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, recipient, amount):
    if coin == ETH:
         tx = create_tx(coin, account, recipient, amount)
         signed_tx = account.sign_transaction(tx)
         result = w3.eth.sendRawTransaction(signed_tx.rawTransaction) #This sends the ether transaction
         print(result.hex())
         return result.hex()

    elif coin == BTC:
        tx = create_tx(coin, account, recipient, amount)
        signed_tx = account.sign_transaction(tx)
        result = NetworkAPI.broadcast_tx_testnet(signed)


