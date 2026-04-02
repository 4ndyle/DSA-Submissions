"""
Input: list (nums)
Output: integer (longest length of consequetive sequence of elements)
Constraints:
    - consequetive sequence is a sequence of elements where each element is exactly 1 greater than the previus element

Plan: Convert the nums list to a nums set. Then, iterate through each num in the nums set. If a num is a starting num, then we want to check if it's preceding values are in the set or not. Increment the length count everytime a preceding value is in the set, otherwise continue on with the next number.

Psuedo Code:
Convert the nums list to a nums set
maxLength = 0

for num in numsSet:
    If num-1 not in set (it's a starting number):
        currentLength = 1

        while num+1 in set:
            increment currentLength
            num += 1

        maxLength = max(currentLength, maxLength)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if num-1 not in numSet:
                currentLength = 1

                while num+1 in numSet:
                    currentLength += 1
                    num += 1

                maxLength = max(currentLength, maxLength)

        return maxLength