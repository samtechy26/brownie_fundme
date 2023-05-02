from brownie import FundMe, accounts, config

def main():
    fund_me = FundMe[-1]
    account = accounts.add(config["account-keys"]["private-keys"])
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding..........")
    fund_me.fund({"from":account, "value":entrance_fee})

