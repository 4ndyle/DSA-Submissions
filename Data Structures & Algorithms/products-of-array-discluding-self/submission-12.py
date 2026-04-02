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

[1,2,4,6]
products from left : [1, 2, 8, 48]
products from right: [48, 48, 24, 6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate the product of all nums
        product = 1
        zerosCount = 0

        for num in nums:
            if num == 0:
                zerosCount += 1
                continue

            product *= num

        print(product)
        print(zerosCount)

        # iterate through nums and calculate output[i]
        output = [0 for i in range(len(nums))]
        print(output)
        
        if zerosCount >= 2:
            return output

        print("- - - - - - -")

        for i in range(len(nums)):
            currNum = nums[i]
            print(currNum)

            if zerosCount > 0:
                print("zeros > 0")
                if currNum == 0:
                    output[i] = product

                continue 

            output[i] = product // nums[i]
            print(product // nums[i])
            print()

        return output

