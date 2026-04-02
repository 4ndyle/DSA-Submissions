class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        start = 1
        end = max(piles)
        minK = float('inf')

        while start <= end:
            middle = (start + end) // 2
            time = 0

            # check each element to calculate time 
            for pile in piles:
                time += math.ceil(pile / middle)

            print(f"time - {time} hours")
            if time > h:
                # search right (decrease time by eating more)
                start = middle + 1
            else:
                # search left (increase time by eating less)
                end = middle - 1
                minK = min(minK, middle)

        return minK


            






        return 2