"""
Input:
    - List[int] : nums
Output:
    - int : lengh of the longest consecutive sequence of elements that can be formed
Constraints:
    - length of nums: [0,100000]
    - values of nums: [-10^9, 10^9]

Idea:
Check if num[i] - 1 is in the list or not. If it is not, then it is the start
of a conseq sequence. Increment until it is no longer conseq. 

Plan:
1. Add all numbers in nums to a set
2. Create variables
    - length = 1
3. for num in numSet:
        if num - 1 not in numSet:
            continue incrementing current number until no longer conseq
            update length
4. Return length
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        length = 0

        for num in numSet:
            # if it is the start of a sequence, calculate the length
            if num - 1 not in numSet:
                currLength = 1

                while num + 1 in numSet:
                    currLength += 1
                    num += 1
                
                length = max(currLength, length)

        return length

