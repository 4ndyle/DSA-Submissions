"""
Input: 
    - List[int] : piles
    - int : h 
Output:
    - int : min integer where you can eat all the bananas

Note:
    - May decide bananas per hour eating rate of k

Examples:


Plan:
1. Find the max pile value in the piles
2. Perform a binary search on the range 1 to max(piles) 
    - if the current mid value can eat all banas in under h hours, search left for a smaller value
    - if koko cannot finish all bananas in under h hours, search right (increase the k banas per hour)
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = float("inf")

        # binary search to find k    
        left = 1 
        right = max(piles)

        while left <= right:
            # mid is the current k number of bananas  
            mid = (left + right) // 2
            hours = 0 

            # find the total number of hours for the current k 
            for pile in piles:
                hours += math.ceil(pile / mid)

            # update the search range 
            if hours > h:
                left = mid + 1
            else:
                k = min(k, mid)
                right = mid - 1

        return k



    