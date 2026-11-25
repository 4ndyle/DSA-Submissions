"""
Input:
    - int : n
Output:
    - int : distict ways to climb to the top of staircase
Constraints:
    - can take 1 or 2 steps at a time
    - range of n: [1,45]a

Plan:
Memoization 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def totalWays(n):
            nonlocal memo 

            if n in memo:
                return memo[n]
            if n <= 1:
                return 1

            # update memo cache 
            total = totalWays(n - 1) + totalWays(n - 2) 
            memo[n] = total 

            return total

        return totalWays(n)