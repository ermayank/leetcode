class Solution:
    def compress(self, chars: List[str]) -> int:
        indexAns, i = 0, 0
        
        while i < len(chars):
            currChar = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == currChar:
                i += 1
                count += 1
                
            chars[indexAns] = currChar
            indexAns += 1
            
            if count > 1:
                for c in str(count):
                    chars[indexAns] = c
                    indexAns += 1
            
        return indexAns
        
        