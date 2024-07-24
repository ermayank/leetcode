/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */

// Done by 2 Pointer Approach O(n) 

var twoSum = function(numbers, target) {
    let l = 0;
    let r = numbers.length - 1;
    
    while(l < r){
        let currSum = numbers[l] + numbers[r]
        if (currSum > target){r = r - 1}
        else if(currSum < target){l = l + 1}
        else return [l+1, r+1]
    }
    
};