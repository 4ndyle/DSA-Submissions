class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            currentNumber = nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            # find two numbers where currentNumber + num1 + num2 = 0
            left = i+1
            right = len(nums) - 1

            while left < right:
                sum = currentNumber + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    # add to our results
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return result