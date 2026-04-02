class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h == len(list):
        #     return max(list)

        piles.sort()
        print(piles)

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
                print("search right")
                start = middle + 1
            else:
                print("searching left")
                end = middle - 1
                minK = min(minK, middle)

            print("")        

        return minK


            






        return 2