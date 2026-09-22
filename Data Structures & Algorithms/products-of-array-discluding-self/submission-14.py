"""
Input:
    - List[int] : nums
Output:
    - List[int] : product of all elements except nums[i]
Constraints:
    - each product fits in a 32-bit integer 
    - length of nums: [2,100000]
    - values of nums: [-30,30]

Using division modulo
1. Get product of all numbers 
    - keep count of number of zeros 
        if there are more than 2 zeros, all nums[i] = 0
        otherwise, skip the one zero when calculating products
2. Create list of len(nums) 0's and calculate the products 
    - reuslt[i] = totalProduct / nums[i]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1    
        totalZeros = 0

        for num in nums:
            if num == 0:
                totalZeros += 1
                continue
            
            totalProduct *= num

        result = [0] * len(nums)

        # return all 0's if there are more than 1 zeros in the nums
        if totalZeros > 1:
            return result

        for i in range(len(nums)):
            if totalZeros < 1 and nums[i] != 0:
                result[i] = int(totalProduct / nums[i])
                continue
            elif nums[i] == 0:
                result[i] = totalProduct

        return result
