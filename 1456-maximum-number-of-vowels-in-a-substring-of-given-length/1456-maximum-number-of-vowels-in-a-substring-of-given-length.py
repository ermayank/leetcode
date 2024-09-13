class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        maxLength = 0
        
        vowels = ("a", "e", "i", "o", "u")
        
        # Count Vowels in initial Window
        for i in range(k):
            if s[i] in vowels:
                res +=1
        
        maxLength = res
            
        for i in range(k, len(s)):
            if s[i] in vowels:
                res += 1
            if s[i-k] in vowels:
                res -= 1
            maxLength = max(res, maxLength)
        
        return maxLength
        