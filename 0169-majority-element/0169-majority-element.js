/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    
    //n = length of array
    let n = nums.length
    
    let numbers = {}
    
    for (let i=0; i<n; i++){
        numbers[nums[i]] = numbers[nums[i]]+1 ||  1
    
        if(numbers[nums[i]] > n/2){
            return nums[i]
        }
    }
   
};