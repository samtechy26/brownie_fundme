from brownie import network, accounts, exceptions, config, FundMe, exceptions
import pytest

def test_can_fund_and_withdraw():
    account = accounts.add(config["account-keys"]["private-keys"])
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from":account, "value":entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

# def test_only_owner_can_withdraw():
#     fund_me = FundMe[-1]
#     bad_actor = accounts.add()
#     with pytest.raises(exceptions.VirtualMachineError):
#         fund_me.withdraw({"from":bad_actor})