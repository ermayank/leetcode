/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let j = s.length - 1
    let i=0
    while(i<j){
        //Swap Elements
        let el = s[i]
        s[i] = s[j]
        s[j] = el
        i++
        j--
    }
    
//     for(let i=0; i< s.length; i++){
        
//         if (i=j || i>j){
//             return s
//         }
        
//         //Swap Elements
//         let el = s[i]
//         s[i] = s[j]
//         s[j] = el
//         j--
        
//     }
};