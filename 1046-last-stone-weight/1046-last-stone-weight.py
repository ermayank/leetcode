class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python does not have max heap so every value is multiplied by -1 and all this confusion arises.

        stones = [-s for s in stones] 
        heapq.heapify(stones)

        while len(stones) > 1:
            #First would be largest but smallest because of min heap
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # Think closely in negative values for min heap but solving problem in max heap
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
        