class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiplied all elements in nums, excluding 0 
        product, zeros = 1,0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        print(product)
        # return output of all zeros if zero count is more than 1
        if zeros > 1:
            return [0] * len(nums)

        # iterate through nums, divide by current num for output[i]
            # if current number is 0, output[i] = product
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = product
            elif zeros < 1:
                res[i] = product // nums[i]


        print(res)

        return res

