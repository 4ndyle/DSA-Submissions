"""
Input:
    - List[int] : piles 
    - int : h 
Output:
    - int : min intreger k such that you can eat all the banaas within h hours 

Plan:
Perform a binary search on possible k's: 
[1, max(piles)]
"""
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minK = float("inf")

        while left <= right:
            currK = (left + right) // 2

            # calculate hours it takes to finish all piles
            totalHours = 0 

            for num in piles:
                totalHours += math.ceil(num / currK)

            print(f"total hours for {currK} = {totalHours} hours")

            # update binary search pointers 
            if totalHours > h:
                left = currK + 1
            elif totalHours <= h:
                minK = min(minK, currK)
                right = currK - 1

        return minK