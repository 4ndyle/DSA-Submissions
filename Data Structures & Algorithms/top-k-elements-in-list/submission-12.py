"""
Input: array (nums), integer (k)
Output: list (k most frequent elements within the array nums)
Constraints:
    - answer is always unique 
    - output in any order
Edge Cases:
    - [] : []

Plan: 
1. Create a dict to map the frequency of each element 
2. Create a array of length nums+1 to represent "buckets", where 
each index represents the frequency. 
3. Iterate through the buckets in reverse order and add the top k
elements with the highest frequencies 
4. return the list of k elements
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map the frequency of each element in nums
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        # create the buckets array
        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            buckets[freq].append(num)

        # iterate through the array in reverse order and get the top elements\
        result = []

        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)

                if len(result) == k:
                    return result


