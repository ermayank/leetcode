/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let numsMap = {};
    let freqArray = [];
    
    // Create map for number frequency
    for(let i = 0; i < nums.length; i++){
        numsMap[nums[i]] = (numsMap[nums[i]] || 0) + 1;
    }
    
    // Index of freqArray is number of times number occurs
    Object.keys(numsMap).forEach((n) => {
        const freq = numsMap[n];
        if (typeof freqArray[freq] === 'undefined') {
            freqArray[freq] = [];
        }
        freqArray[freq].push(parseInt(n));
    });
    
    let res = [];
    for(let i = freqArray.length - 1; i >= 0; i--){
        if (typeof freqArray[i] !== 'undefined') {
            freqArray[i].forEach((e) => res.push(e));
        }
        
        if (res.length >= k) {
            return res.slice(0, k);
        }
    }
    return res;
};