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
        # find the max value in the piles
        maxBananas = max(piles)

        # create a variable to keep track of the lowest k
        k = maxBananas
        
        # perform a binary search on the range 1 to maxBananas to find the min k
        left = 1
        right = maxBananas

        while left <= right:
            # the mid represents the k bananas per hour
            mid = (left + right) // 2
            print(f"checking {mid}")


            # go through piles and check if the current k (mid) is valid
            currHours = 0

            for pile in piles:
                currHours += math.ceil(pile / mid)

            print(f"It takes {currHours} to eat all bananas")
            # search left when we have a valid k to see if we can find a lower k and update k
            if currHours <= h:
                print(f"Searching left to find better k")
                k = min(k, mid)
                right = mid - 1
            else:
            # search right when we cannot eat all bananas (need to increase bananas we eat)
                print(f"Searching right to consume more bananas")
                left = mid + 1

        return k    



    