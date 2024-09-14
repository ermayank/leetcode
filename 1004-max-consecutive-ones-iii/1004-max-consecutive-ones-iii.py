class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxWidth = 0
        zeros = 0
        l = 0
        
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            width = r - l + 1
            maxWidth = max(maxWidth, width)
        
        return maxWidth
                
            
            
            
        