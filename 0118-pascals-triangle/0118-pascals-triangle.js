/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let output = [];
    
    if (numRows == 0) {
        return output
    }
    output.push([1])
    
    //loop till num rows
    for (let i=1; i<numRows; i++) {
        let inner = [1]
        for (let j=1; j<=i-1; j++){
           let sum = output[i-1][j-1] + output[i-1][j]
           inner.push(sum)
        }
        inner.push(1)
        output.push(inner)
    }
    return output
};
