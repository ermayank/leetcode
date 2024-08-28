class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        sPointer = 0
        
        for i in range(0, len(t)):
            if sPointer < len(s) and s[sPointer] == t[i]:
                sPointer += 1
        
        return sPointer == len(s)
                
        