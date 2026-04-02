class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numFreq = {}

        for num in arr:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        print(numFreq)
        luckyNum = -1

        for num, freq in numFreq.items():
            if num == freq:
                luckyNum = max(luckyNum, num)

        return luckyNum

        