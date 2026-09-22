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

Using prefix and suffix 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find the prefix
        prefix = []
        prefixProduct = 1

        for num in nums:
            prefix.append(prefixProduct)
            prefixProduct *= num

        # find the suffix 
        suffix = []
        suffixProduct = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix.append(suffixProduct)
            suffixProduct *= nums[i]
        
        # calculate the results
        result = prefix 
        prefixIndex = 0 

        for i in range(len(suffix) - 1, -1, -1):
            result[prefixIndex] *= suffix[i]
            prefixIndex += 1

        return result