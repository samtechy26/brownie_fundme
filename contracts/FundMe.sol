// SPDX-License_Identifier: MIT
pragma solidity ^0.6.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;
    constructor() public {
        owner = msg.sender;
    }
    function fund() public payable {
        uint256 minimumUSD = 50 * 10 ** 18;
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more Eth");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);

        // what the ETH -> USD conversion rate is 

    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        priceFeed.version();
    }

    function getPrice() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        priceFeed.latestRoundData();
        
    }
// 1000000
    function getConversionRate(uint256 ethAmount) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 10000000000000000000;
        return ethAmountInUSD;
    }

    modifier  onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function withdrawal() payable onlyOwner public {
        //only want the contract owner to be able to withdraw funds
        
        msg.sender.transfer(address(this).balance);
        for  (uint256 funderIndex = 0; funderIndex < funders.length; funderIndex++){
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }

}