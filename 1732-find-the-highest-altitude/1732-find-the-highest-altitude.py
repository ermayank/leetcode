class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        maxAlt = 0
        
        for i in range(len(gain)):
            el = alt[i] + gain[i] 
            alt.append(el)
            maxAlt = max(maxAlt, el)
        
        return maxAlt
        