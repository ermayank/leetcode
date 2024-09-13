class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def isDivisor(l):
            # Is l fator of both strings
            if len1 % l or len2 % l:
                return False
            factor1, factor2 = len1 // l, len2 // l
            return str1[:l]*factor1 == str1 and str1[:l]*factor2 == str2
        
        for l in range(min(len1,len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""