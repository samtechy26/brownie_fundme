from brownie import FundMe, MockV3Aggregator, network, config, accounts

DECIMALS = 8
# This is 2,000
STARTING_PRICE = 200000000000

def deploy_mocks():
    account = accounts.add(config["account-keys"]["private-keys"])
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
    print("Mocks Deployed!")

def main():
    account = accounts.add(config["account-keys"]["private-keys"])
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(price_feed_address, {"from":account})
    print(f"Contract deployed to {fund_me.address}")
    