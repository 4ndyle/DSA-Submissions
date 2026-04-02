class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)    

        #    prefix 
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        print(res)


        # postfix 
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        print(res)

        return res
