class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for num in numSet:
            
            # if num - 1 does not exist, we know that it is the start of a sequence
            if num - 1 not in numSet:
                # check for sequential numbers by iterating through current number and add one each time 
                currentLength = 1

                while num + currentLength in numSet:
                    currentLength += 1
                
                # update longest
                longest = max(currentLength, longest)

        return longest