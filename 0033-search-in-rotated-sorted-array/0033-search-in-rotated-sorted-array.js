/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0
    let r = nums.length - 1
    
    while(l <= r)
    {
        let mid = l + ((r - l) >> 1)
        if(target == nums[mid]) { return mid }
        
        //Left Sorted
        
        if(nums[l] <= nums[mid]){
            if (target > nums[mid] || target < nums[l]) {
                l = l = mid + 1
            }
            else{
            r = mid - 1    
            }
        }
        
        //Right Sorted 
        else{
            if (target < nums[mid] || target >  nums[r]){
                r = mid - 1
                }
            else{
                l = mid + 1
            }
        }

          }
    return -1
};