class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        # O(n)
        maxVal = max(candies)
        
        for c in candies:
            res.append(c + extraCandies >= maxVal)
        
        return res