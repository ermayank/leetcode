/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let l = 0
    let r = Math.max(...piles)
    let res = r
    
    while(l <= r){
        let k = Math.floor((l + r) / 2)
        let hours = 0
        
        for(let i of piles){
            hours += Math.ceil(i / k) 
        }
        
        if(hours <= h){
            res = Math.min(res, k)
            r = k - 1
        }
        else {
            l = k + 1
        }
    }
    return res
};