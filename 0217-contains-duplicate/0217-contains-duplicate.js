/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let numbersMap = {}
    
    for(let i = 0; i< nums.length; i++){
        numbersMap[nums[i]] = numbersMap[nums[i]]+1 || 1 
        if (numbersMap[nums[i]] > 1){
            return true
        }
    }
    return false
    
    
};