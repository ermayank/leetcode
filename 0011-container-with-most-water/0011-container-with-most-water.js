/**
 * @param {number[]} height
 * @return {number}
 */

//Edge case when both height are same check next val to shift or shift anyone

var maxArea = function(height) {
    let res = 0
    let l = 0
    let r = height.length - 1
    
    while(l < r){
        let area = Math.min(height[l] , height[r]) * (r - l)
        res = Math.max(res, area)
        
        if(height[l] < height[r]){l += 1}
        else if(height[l] > height[r]){r -= 1}
        else {
            (height[l] > height[l+1] ? r-=1 : l+=1)
        }
        
    }
    return res
    
};