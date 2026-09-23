"""
Input:
    - List[int] : nums
Outout
    - List[List[int]] : nums[i] + nums[j] + nums[k] ==  0
Constraints:    
    - no duplicate triplets
    - possible length of nums: [3,3000]
    - possible values of nums: [-10^5, 10^5]

Plan:
1. Sort the input nums in ascending order
2. Create variables
    - results = []
3. for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] < 0:
                increment left pointer
            elif nums[i] + nums[left] + nums[right] > 0:
                decrement right pointer
            else:
                add triplet to results

                increment left 
                continusly increment left if it is equal to the prev (avoid duplicates)
4. Return results
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            # search for 2 other numbers that sum with nums[i] to get 0
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
            

                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return results

"""
Example:
Input = [-1,0,1,2,-1,-4]
Sorted = [-4, -1, -1, 0, 1, 2]
           ^          L     R
"""