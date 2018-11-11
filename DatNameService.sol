pragma solidity ^0.4.25;

import "./Ownable.sol";

contract DatNameService is Ownable {
    
    mapping (string => string) private datURLs;
    
    function addDat(string _datName, string _URL) public onlyOwner {
        datURLs[_datName] = _URL;
    }
    
    function removeDat(string _datName) public onlyOwner {
        datURLs[_datName] = "";
    }
    
    function getDatURL(string _datName) public view returns(string URL) {
        URL = datURLs[_datName];
    }
}
