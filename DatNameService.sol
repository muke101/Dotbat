pragma solidity ^0.4.25;

import "./Ownable.sol";

contract DatNameService is Ownable {
    
    mapping(string => string) private datId;
    
    function addDatName(string _name, string _datId) public onlyOwner {
        datId[_name] = _datId;
    }
    
    function removeDatName(string _name) public onlyOwner {
        datId[_name] = "";
    }
    
    function getDatId(string _name) public view returns(string) {
        return datId[_name];
    }
}
