class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxWidth = 0
        zeros = 0
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            width = r-l+1
            maxWidth = max(maxWidth, width-zeros)
        
        return maxWidth if maxWidth != len(nums) else len(nums) - 1
        