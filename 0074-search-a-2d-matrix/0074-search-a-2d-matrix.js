/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    //Two Binary Search
    let ROWS = matrix.length
    let COLS = matrix[0].length
    
    //1. Get the target Array/Row
    let topRow = 0
    let botRow = ROWS - 1
    
    while(topRow <= botRow){
        let currRow = Math.floor((topRow + botRow) / 2)
        
        if(target > matrix[currRow][COLS - 1])
            {topRow = currRow + 1}
        else if(target < matrix[currRow][0]) 
            {botRow = currRow - 1}
        else {break}
    }
    
    if (topRow > botRow){
        return false
    }
    
    //2. Get the target Number
    let low = 0
    let high = COLS - 1
    let currRow = Math.floor((topRow + botRow) / 2)
    
    while(low <= high){
        let mid = Math.floor((high + low) / 2)
        
        if(target > matrix[currRow][mid]){low = mid + 1}
        else if(target < matrix[currRow][mid]){high = mid - 1}
        else {return true}
    }
    return false
};
