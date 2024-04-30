/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let count = 0;
    let numBin = n.toString(2);
    
    //Normal Loop
    // for(let c of numBin){
    //  if (c === '1') count++   
    // }
    // return count
    
    // Bitwise Shifting
        while (n !== 0) {
        const bitComparison = n & 1; // 1 & 1 will return 1. 0 & 1 will return 0.
        if (bitComparison === 1) count++;
        n >>>= 1; // unsigned right shift assignment (chop off the last bit and assign it)
    }  
    return count
};