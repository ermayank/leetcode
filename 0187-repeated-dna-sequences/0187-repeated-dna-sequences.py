class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        strings = set()

        # Initial Window
        sub = s[:10]
        strings.add(sub)
        newSub = sub

        for i in range(10, len(s)):
            newSub = newSub + s[i]
            newSub = newSub[1:]
            print(i, newSub)

            if newSub in strings:
                res.add(newSub)
            else:
                strings.add(newSub)
        
        return res


        



        