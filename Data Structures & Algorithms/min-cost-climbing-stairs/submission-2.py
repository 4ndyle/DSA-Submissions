"""
Input:
    - List[int] : cost
Output:
    - int : min cost to reach the top of the staircase
Constraints:
    - can only take 1 or 2 steps from each position
    - start before index 0
    - range of cost: [0,100]
    - length of cost: [2,100]

Plan:
1. Start by choosing the smallest cost at index 0 or 1
2. At each iteration, look ahead at the next 2 steps and choose the index with the
lowest cost
3. When at the top, choose to go past the last step if possible 
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        memo = {}        

        def minCost(index):
            nonlocal memo 

            if index < 0:
                return 0
            if index in memo:
                return memo[index]

            memo[index] = min(minCost(index - 1), minCost(index - 2)) + cost[index]
            return memo[index]

        return min(minCost(len(cost) - 1), minCost(len(cost) - 2))


