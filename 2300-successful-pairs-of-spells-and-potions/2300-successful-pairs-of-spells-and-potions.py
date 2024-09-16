class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # nlog(n)
        potions.sort()
        
        res = []
        
        for i in range(len(spells)):
            l,r = 0, len(potions) - 1
            
            while l <= r:
                mid = l + ((r - l)//2)
                curr = potions[mid]*spells[i]
                if curr >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            
            res.append(len(potions) - 1 - r)
        
        return res
           
                
            
            
            
            