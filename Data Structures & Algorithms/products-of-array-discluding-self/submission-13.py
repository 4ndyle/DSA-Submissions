"""
Input: 
    - List[int] : nums
Output
    - List[int] : where output[i] is the product of all elements expcept itself
Constraints
    - -20 <= nums[i] <= 20
    - 2 <= nums.length <= 1000

Apporaches:
1. Get the product of all numbers in the array and divide by the number at index i to 
get the num[i] (division is inverse operation of multiplication)

Examples:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

input: [1,2,4,6]
products from left : [1, 2, 8, 48]
products from right: [48, 48, 24, 6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find the prefix products 
        prefix = [nums[0]] * len(nums)
        # print(prefix)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        print(prefix)

        # find the suffix products 
        suffix = [nums[-1]] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        output = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                output[i] = suffix[i+1]
            elif i == len(nums) - 1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * suffix[i+1]

        return output
