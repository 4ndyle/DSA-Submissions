"""
Input: 
    - List[Int] : piles
    - int : h (hours to eat the bananas)
Output:
    - int : k (bananas per hour)
Constraints:
    - 1 <= piles.length <= 1000
    - piles.length <= h <= 1000000
    - 1 <= piles[i] <= 1000000000

"""

import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        left = 1
        right = maxPile
        k = 0

        while left <= right:
            # the middle pointer is our current banana eating rate
            mid = (left + right) // 2 

            currHours = 0

            # simulate the banana eating and check if it is within the h time input
            for pile in piles:
                currHours += math.ceil(pile / mid)

            # use a binary search to find values of bananas per hour rate 
            if currHours <= h:
                # valid k, search left for potential smaller min integer k
                k = mid
                right = mid - 1
            else:
                left = mid + 1

        return k
