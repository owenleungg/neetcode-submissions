class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        DP = [0, 0] # lowest cost to reach floor i

        for i in range(2, len(cost) + 1):
            DP.append(min(DP[i-1] + cost[i - 1], DP[i-2] + cost[i - 2]))
        
        return DP[len(cost)]