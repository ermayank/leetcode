/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    
        let n = nums.length
        
        if(n == 0){
            return 0
        }
    
    
    //Sum of nth Array - Sum of Actual Array
    

    let arraySum = (n*(n+1))/2;
    let actualSum = 0;
    
    for(let i=0; i<n; i++){
        actualSum += nums[i]
    }
    
    return arraySum - actualSum
};