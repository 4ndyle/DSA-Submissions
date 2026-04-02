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

        # indexes with value 0 are the total product
        newList = []

        for i in range(0,len(nums)):

            if nums[i] == 0:
                newList.append(product)

            elif 0 in nums:
                newList.append(0)

            # total product divided by value at index
            else:
                newList.append((int)(product / nums[i]))

        return newList