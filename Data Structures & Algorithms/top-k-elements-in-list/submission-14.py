"""
Input:
    - List[int] : nums
    - int : k
Output:
    - List[int] : k most frequent elements in the array
Constraints:
    - test cases always unique and output can be returned in any order 
    - range of values in nums: -1000 <= nums[i] <= 1000
    - range of values for k: 1 <= k <= number of distinct elements in nums
    - length of nums: 1 <= nums.length <= 10^4

Ideas:
    1. Use a dict to map the value to their frequency and iterate through dict to find top k elements
        - Time: O(n) + O(n * k) = O(n * k)
        - Space: O(n) for dict 
    2. Use a dict to map the value to their frequency and use bucket sort to place all values into their 
    buckets where each index the the bucket array represents the frequency 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the frequenncy of each unuique element 
        frequencyDict = {}

        for num in nums:
            frequencyDict[num] = frequencyDict.get(num, 0) + 1

        print(frequencyDict)

        # use bucket sort to place each value into their bucket 
        buckets = [[] for i in range(len(nums) + 1)]

        # sort each element into their respective buckets
        for numsVal, frequency in frequencyDict.items():
            buckets[frequency].append(numsVal)

        print(buckets)

        # find the top k frequent elements by iterating in reverse order
        topKElements = []

        for bucket in reversed(buckets):
            if not bucket:
                continue 

            for numVal in bucket:
                topKElements.append(numVal)

                if len(topKElements) >= k:
                    return topKElements


