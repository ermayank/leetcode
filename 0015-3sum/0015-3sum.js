/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let res = []
    nums = nums.sort((a, b) => a - b)
    
    for(let i = 0 ; i < nums.length - 1 ; i++){
        if(i > 0 && nums[i] == nums[i-1]){
            continue
        }
        //2 Sum
        let l = i + 1
        let r = nums.length - 1
        
        while(l < r){
            sum = nums[i] + nums[l] + nums[r]
            
            if(sum > 0){r -= 1}
            else if(sum < 0){l += 1}
            else{
                res.push([nums[i], nums[l], nums[r]])
                l = l + 1
                while(nums[l] == nums [l - 1] && l < r){
                    l = l + 1
                }
            }
            
        }
    }
    return res
    
};