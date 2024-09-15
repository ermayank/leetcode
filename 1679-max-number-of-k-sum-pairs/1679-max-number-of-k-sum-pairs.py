class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sort Array
        nums.sort()
        count = 0
        
        l,r = 0, len(nums)-1
    
        while l < r:
            numSum = nums[l] + nums[r]
            if numSum == k:
                l += 1
                r -= 1
                count += 1
            elif numSum > k:
                r -= 1
            else:
                l += 1
        
        return count
            
        