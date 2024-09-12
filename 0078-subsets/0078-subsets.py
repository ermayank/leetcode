class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking --> We have 2 decision for every element. Add or not
        
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Add element to the set
            subset.append(nums[i])
            dfs(i+1)
            
            # NOT to add element to the set
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res
        