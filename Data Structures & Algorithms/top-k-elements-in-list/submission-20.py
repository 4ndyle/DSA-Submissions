"""
Input:
    - List<int> : nums 
    - int : k 
Output: 
    - int : k most frequent elements within the array
Constraints:
    - possible length of nums: [1,10^4]
    - possible values of nums: [-1000, 1000]
    - possible values of k: [1, number of distinct elements]

Plan:
1. Create dict and iterate through nums 
    - numsCount = { number : frequency }
2. Create a heap and add each pair (frequency, number) to heap
    - if len(heap) > k:
        pop the min (root) from the heap
        add new pair to heap
3. Create empty list and iterate through the k elements in heap and add number 
4. Return list 
"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        # print(numCount)

        heap = []
        for num, freq in numCount.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)


        # print(heap)

        # extract k nums from the heap 
        result = []
        while heap:
            num = heapq.heappop(heap)[1]
            # print(f"{num}")
            result.append(num)

        return result


        

