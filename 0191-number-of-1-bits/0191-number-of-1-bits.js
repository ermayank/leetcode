/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let count = 0;
    let numBin = n.toString(2);
    for(let c of numBin){
     if (c === '1') count++   
    }
    return count
};