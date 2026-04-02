class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # create set of nums 
        numsSet = set(nums)
        longestLength = 1

        for num in numsSet:
            # check if number is a starting number
            if num-1 not in numsSet: 
                currentNum = num
                length = 1
                # check for increasing 
                while currentNum+1 in numsSet:
                    print(f"found {currentNum}")
                    length += 1
                    currentNum += 1
                
                print(f"length is {length}")
                longestLength = max(longestLength, length)

        return longestLength