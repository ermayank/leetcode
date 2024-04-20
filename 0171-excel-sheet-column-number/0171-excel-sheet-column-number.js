/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    
    // This process is similar to binary-to-decimal conversion
    //Getting Char Code and then subtracting 'A' to get eg B=2
    let result = 0;
    for (let i = 0; i < columnTitle.length; i++)
    {
        result *= 26;
        result += columnTitle[i].charCodeAt(0) - 'A'.charCodeAt(0) + 1;
    }
    return result;
    
};