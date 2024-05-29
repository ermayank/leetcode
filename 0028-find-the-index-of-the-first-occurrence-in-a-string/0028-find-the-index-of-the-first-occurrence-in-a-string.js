/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
  let hlen = haystack.length 
  let nlen = needle.length 
  let npointer = 0

  for (let i = 0; i < hlen; i++) {

    if (haystack[i] == needle[npointer]) {
      npointer++
    } else {
        i = i-npointer;
       npointer = 0
    }

    if (npointer == nlen) {
      return (i - nlen + 1)
    }
  }
  return - 1
};