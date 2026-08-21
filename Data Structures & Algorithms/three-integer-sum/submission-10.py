"""
Input:
    - List[int] : nums
Output:
    - List[List[int]] : [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] = 0
Constraints
    - output should not contain dupliate triplets
    - length of nums: [3,3000]
    - values of nums: [10^-5, 10^5]
Plan:
    1. Sort the array nums in ascending order
    2. Create a set containing the total triplets
    3. Create for loop to iterate through the list (i)
        Use a left and right pointer to find 2 numbers occuring after i 
            - if triplets sum to 0, add triplet tuple to set 
    4. Convert the set to a list and tuples to lists
    5. Return result
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array in ascending order
        nums.sort()

        # create a set containing the total triplets
        tripletSet = set()

        for i in range(len(nums)):
            # skip the numbers that are duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # find 2 other numbers that sum with nums[i] to equal 0
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum == 0:
                    tripletSet.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
                
        # convert the triplet set into a list and tuples into a list 
        print(tripletSet)
        return list(tripletSet)






                