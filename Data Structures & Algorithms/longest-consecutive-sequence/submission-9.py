class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # base case: if list is empty
        if len(nums) == 0:
            return 0


        # convert array into hashset 
        numSet = set(nums)
        print(numSet)
        maxTotal = 0

        for num in numSet:
            # check if number has left neighbor 
            if num-1 not in numSet:
                length = 1
                while num+length in numSet:
                    length += 1
                
                maxTotal = max(length, maxTotal)
            

        return maxTotal