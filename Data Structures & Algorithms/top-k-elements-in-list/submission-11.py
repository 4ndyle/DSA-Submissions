"""
Input: list (nums), integer k
Output: list (k most frequent elements in the array nums)
Constraints:
    - may return output in any order
Edge Cases:
    - k = 0 -> return []

Plan: Iterate through the nums list and use a dict to map the frequency of each number. 
Then create a list of empty lists of length nums where each empty list represents a bucket and the index is it's frequency. Iterate through the dict and append each
element to the empty list (or bucket) at their respective frequencies. 

Psuedo Code:
Create a dict to keep track of the frequency of each num

for num in nums:
    get the default value of num in the dict and increment it

Create a list of empty lists(buckets) to store each num based on their frequency
frequencyBucket = [[]] * len(nums)+1

for num, frequency in dict.items():
    append the current number to it's empty list (bucket) in the frequencybucket list based on it's frequency

res = []
for bucket in reversed(frequencyBucket):
    if the bucket has elements and the len(res) is less than k, add the element to results list

return the results list
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the frequency count
        numCount = {}

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        print(numCount)
        # map the frequency count to it's bucket
        frequencyBucket = [[] for i in range(len(nums) + 1)]

        for num, frequency in numCount.items():
            frequencyBucket[frequency].append(num)

        print(frequencyBucket)
        # iterate through the buckets in reverse order and find the top k elements
        res = []

        for bucket in reversed(frequencyBucket):
            while bucket and len(res) < k:
                res.append(bucket.pop())

                if len(res) == k:
                    return res

        


        