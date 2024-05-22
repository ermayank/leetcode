/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {

    const bSearch =  function(arr, low, high, x) {
    if (low > high) {return high+1}
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] == x) {return mid}
    if (arr[mid] > x) {return bSearch(arr, low, mid - 1, x)}
    if (arr[mid] < x) {return bSearch(arr, mid + 1, high, x)}
  }
    
    return bSearch(nums, 0, nums.length - 1, target)

};