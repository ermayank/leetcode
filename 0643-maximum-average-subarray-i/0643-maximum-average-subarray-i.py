class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr =  maxSum = sum(nums[:k])
        
        for i in range(k,len(nums)):
            curr = curr + nums[i] - nums[i-k]
            maxSum = max(curr, maxSum)
        
        return maxSum/k
            
            
        
        
        