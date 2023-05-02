from brownie import FundMe, accounts, config

def main():
    fund_me = FundMe[-1]
    account = accounts.add(config["account-keys"]["private-keys"])
    print(f"withdrawing funds to {account.address}")
    fund_me.withdraw({"from":account})