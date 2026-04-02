class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # compute the total product excluding 0
        product = 1
        zeroCount = 0

        for num in nums: 
            if num != 0:
                product *= num
            else:
                zeroCount += 1

        # edge case - more than two zeros means that everything is zero
        if zeroCount > 1: return [0] * len(nums)

        result = [0] * len(nums)
        # indexes with value 0 are the total product
        for index, value in enumerate(nums):
            if zeroCount > 0:
                if value == 0:
                    result[index] = product
            else:
                result[index] = product // value


        return result