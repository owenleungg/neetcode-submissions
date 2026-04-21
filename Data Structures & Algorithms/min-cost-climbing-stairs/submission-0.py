class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        DP = [cost[0], cost[1]] # lowest cost to leave floor i

        for i in range(2, len(cost)):
            DP.append(min(DP[i-1] + cost[i], DP[i-2] + cost[i]))
        
        return min(DP[-1], DP[-2])