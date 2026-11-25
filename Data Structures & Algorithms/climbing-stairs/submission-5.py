"""
Input:
    - int : n
Output:
    - int : distict ways to climb to the top of staircase
Constraints:
    - can take 1 or 2 steps at a time
    - range of n: [1,45]a

Plan:
Dynamic Programming using an array
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]




