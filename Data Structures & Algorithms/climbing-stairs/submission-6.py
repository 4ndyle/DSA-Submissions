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
        if n <= 1:
            return 1

        dp = [0] * (n + 1)

        prev1, prev2 = 1, 1
        totalWays = 0 

        for i in range(2, n+1):
            totalWays = prev1 + prev2

            prev1 = prev2
            prev2 = totalWays 

        return totalWays




