class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        res = []
        
        def dfs(i, curr, total):
            # Base Cases
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # Case 1
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            
            # Case 2
            curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        return res
        