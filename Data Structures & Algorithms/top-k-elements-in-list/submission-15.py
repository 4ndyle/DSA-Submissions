"""
Input:
    # - List[int] : nums
    - int : k
Output:
    - List[int] : k most frequent elements within array
Constraints:
    - length of nums: [1, 10^4]
    - values of nums: [-1000,1000]
    - values of k: [1, num of distinct elemtns in nums]

Plan:
1. Create dict and get count of each element
2. Create list of [] of lenegth len(nums) + 1
3. Add each num in dict to index corresponding to count
4. iterate through countList in reverse order 
    - add k numbers to results
5. Return results
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency of each element
        numCount = {}

        for currNum in nums:
            numCount[currNum] = numCount.get(currNum, 0) + 1

        # group each element into corresponding frequency
        frequencyIndex = [[] for i in range(len(nums) + 1)]

        for num, count in numCount.items():
            frequencyIndex[count].append(num)

        # find the top k elements 
        result = []

        for i in range(len(frequencyIndex) - 1, -1, -1):
            for num in frequencyIndex[i]:
                result.append(num)

                if len(result) == k:
                    return result