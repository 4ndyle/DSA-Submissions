class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set of nums 
        numsSet = set(nums)
        longestLength = 0

        for num in numsSet:
            # check if number is a starting number
            if num-1 not in numsSet: 
                length = 1
                # check for increasing 
                while num+length in numsSet:
                    length += 1
                
                longestLength = max(longestLength, length)

        return longestLength