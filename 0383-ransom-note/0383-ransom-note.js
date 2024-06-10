/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    if (ransomNote.length > magazine.length) return false;
    
    let magCount = {}
    
    for(let i = 0 ; i < magazine.length ; i++){
        magCount[magazine[i]] = magCount[magazine[i]] + 1 || 1
    }
    
    for(let j = 0 ; j<ransomNote.length ; j++){
        //No character present -> return False
        if(!magCount[ransomNote[j]] || magCount[ransomNote[j]] <= 0) {
            return false 
        }else{
            magCount[ransomNote[j]] -= 1  
        }
    }
    return true
    
    
};