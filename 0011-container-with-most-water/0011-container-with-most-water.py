class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        maxArea = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(area, maxArea)
            
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                # Little optimization if same
                l, r = (l + 1, r) if height[l] < height[l+1] else (l, r - 1)
            
        return maxArea
        