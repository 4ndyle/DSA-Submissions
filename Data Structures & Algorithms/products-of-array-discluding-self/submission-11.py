"""
Input: list (nums)
Output: list (output[i] is product of all elements except nums[i])
Constraints:
    - output[i] is the product of all elements except itself
Edge Cases:
    - empty list -> []

Plan: Find the total product of all elements in the list. Iterate through each num
in the list and divide total product of all elements by the current element to get 
output[i]. Return the output
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        containsZero = False

        for num in nums:
            if num != 0:
                totalProduct *= num
            else:
                if containsZero:
                    totalProduct *= 0
                else:
                    containsZero = True

        print(totalProduct)

        for i in range(len(nums)):
            if containsZero:
                if nums[i] == 0:
                    nums[i] = totalProduct
                else:
                    nums[i] = 0
            else:
                nums[i] = int(totalProduct / nums[i])

        return nums

