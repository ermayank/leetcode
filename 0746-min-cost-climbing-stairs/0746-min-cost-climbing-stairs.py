class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Simplify the computation
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            oneStepCost = cost[i] + cost[i+1]
            twoStepCost = cost[i] + cost[i + 2]
            
            cost[i] = min(oneStepCost, twoStepCost)
            
        return min(cost[0], cost[1])
            