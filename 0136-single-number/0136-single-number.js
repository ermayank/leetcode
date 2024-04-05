/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    //Hash Map
//     let ht = {}
    
//     for(let i of nums){
//         ht[i] = ht[i] + 1 || 1
//     }
    
//     for(key in ht){
//         if (ht[key] == 1){ 
//             return key
//         }
       
//     }
    
    //XOR Operator
    
    let ans;
    for (let i of nums) {
        ans^=i;
        
    }
    return ans

};