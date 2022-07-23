from brownie import SimpleStorage, accounts, config

# read_contract function retrieves the most recent deployment of the Simple Storage contract
def read_contract():

    # Take the index that's one less than the length to work with the most recent deployment
    simple_storage = SimpleStorage[-1]
    # ABI
    # Address
    print(simple_storage.retrieve())

def main():
    read_contract()