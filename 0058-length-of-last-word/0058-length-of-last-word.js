/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let wordLength = 0
    
    for(let i = s.length - 1 ; i >= 0 ; i--){
        
        if(s[i] !== " "){wordLength ++}
        else {
            if(wordLength > 0){ return wordLength}
        }
    }
    return wordLength
};