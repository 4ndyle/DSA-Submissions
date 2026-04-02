"""
Input:
    - List[int] : 
Output:
    - int : length of the longest consecutive sequence of elements that can be formed 

Consequtive seq : seq of elements in which each element is exactly 1 greater than the prev

Constraints:
    - Time: O(n)
    - Lenght of nums: 0 <= length <= 1000
    - Values of nums: -10^9 <= num[i] <= 10^9

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4

check if currNum - 1 is in the nums or not (kept track by set)

If there is currNum - 1 in this set, we know that it is a sequence of at least 2. Then 
continue incrementing while the number is in the set

WAIT NO

Find the start of the sequence (when a number does not have a prev)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set to keep track of the numbers
        seenNums = set()

        # iterate through array to record numbers in nums for O(1) search time
        for num in nums:
            seenNums.add(num)

        # for each element in the set, check if it has a prev element, if it does, increment 
        # and record the length of the length
        longestLen = 0 

        for num in nums:
            # find the start of the sequence
            if num - 1 not in seenNums:

                # find the total length of the sequence from start
                sequenceLen = 0
                currNum = num

                while currNum in seenNums:
                    sequenceLen += 1
                    currNum += 1

                longestLen = max(sequenceLen, longestLen)

        return longestLen



                











