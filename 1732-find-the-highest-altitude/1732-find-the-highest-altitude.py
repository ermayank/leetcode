class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = 0
        maxAlt = 0
        
        for i in range(len(gain)):
            prefixSum = prefixSum + gain[i]
            maxAlt = max(prefixSum, maxAlt)
        
        return maxAlt
        