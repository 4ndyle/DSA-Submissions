"""
Input: 
    - List[int] : nums
Output: 
    - List[List[int]] : [nums[i], nums[j], nums[k]] where the sum of all 3 numbers = 0 
    and the triplets must be distinct 
Constraints:
    - triplet must be distinct 
    - all triplets must sum up to 0

Plan: 
1. Brute Force - O(n^3) time complexity 
    - Sort the input and create 3 loops to find 3 numbers that sum up to 0
2. Two Pointer - O(n^2)
    - Sort the input, iterate through each element and use two pointers to find two other elements 
    that sum up to 0 (similar to two sum that is sorted)

Example: 
[0,1,1]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums input 
        nums.sort()
        print(nums)

        # iterate through each element and add each triplet that sums up 0 to set 
        triplets = set()

        for i in range(len(nums)-2):
            firstNum = nums[i]
            print(firstNum)

            # use two pointers on the numbers occuring after the current number to find potential sum
            left = i + 1
            right = len(nums) - 1

            while left < right: 
                if firstNum + nums[left] + nums[right] < 0:
                    left += 1
                elif firstNum + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    triplets.add((nums[i],nums[left],nums[right]))

                    right -= 1


        return list(triplets)





