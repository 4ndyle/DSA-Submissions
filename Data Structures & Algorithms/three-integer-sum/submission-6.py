"""
Input: 
    - nums : List[Int]
Output:
    - List[Int] : list of triplets that sum up to 0
Constraints:
    - output should not contain duplicates
    - 3 <= nums.length <= 1000
    - -10^5 <= nums[i] <= 10^5

Plan: Sort the nums list in acsending order and go through each element in the 
list. Then use two sum on the window of elements occuring after the current 
element to find two numbers that can add up to the current element to be 0. 

[-4, -1, -1, 0, 1, 2]

Psuedo Code:
sort the nums list
res = []

for i in range(len(nums)):
    If the current element is a duplicate, continue until the last occurence

    left = i + 1
    right = len(nums)-1

    while left < right:
        currentSum = nums[i] + nums[left] + nums[right]

        if currentSum is equal to 0:
            add the triple to the list

            update the left and right pointer

            update the left pointer to skip duplicates
            while nums[left] == nums[left-1]:
                left += 1

        otherwise, if the currentSum > 0:
            decrement the right pointer
        else:
            increment the left pointer 

return result
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1

        return res


        