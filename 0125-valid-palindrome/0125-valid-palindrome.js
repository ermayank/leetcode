/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    //Clean the string --> Reverse the string --> Check the reversed string
    
    //AlphaNumeric Function
    function alphaNumeric(c){
        const charCode = c.charCodeAt(0)
        if (!(charCode > 47 && charCode < 58) && // numeric (0-9)
            !(charCode > 64 && charCode < 91) && // upper alpha (A-Z)
            !(charCode > 96 && charCode < 123) // lower alpha (a-z)
           ) {
            return false
        }
        else {return true}
    }
    
    let left = 0 
    let right = s.length - 1 
    
    while(left < right){
        
        while(left < right && !alphaNumeric(s[left])) {left++}
        
        while(left < right && !alphaNumeric(s[right])) {right--}

        if(s[left].toLowerCase() != s[right].toLowerCase()) {return false}
        left++
        right--
    }
    return true
    
};