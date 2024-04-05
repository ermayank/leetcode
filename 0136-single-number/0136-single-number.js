/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let ht = {}
    
    for(let i of nums){
        ht[i] = ht[i] + 1 || 1
    }
    
    for(key in ht){
        if (ht[key] == 1){ 
            return key
        }
       
    }

};