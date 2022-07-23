from turtle import update
from brownie import accounts, config, SimpleStorage, network

# Function deploy_simple_storage() deploys the Simple Storage smart contract.
def deploy_simple_storage():
    # Deploy Contract
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)

    # Update Contract
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

# Function get_account gets the user account if on a local blockchain;
# else it will pull wallet info from the .env file
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()