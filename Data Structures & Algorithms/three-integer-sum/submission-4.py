class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums list in ascending 
        nums.sort()
        print(nums)

        result = []

        for i in range(len(nums)):
            # skip duplicate of i, since we already are checked the value 
            if i > 0 and nums[i-1] == nums[i]:
                continue 

            currentNum = nums[i]
            left = i+1
            right = len(nums) - 1
            
            # applying two sum technique to the current pointer of outside loop
            while left < right:
                currentSum = currentNum + nums[left] + nums[right]

                if currentSum < 0:
                    # increase the sum 
                    left += 1
                elif currentSum > 0: 
                    # decrease the sum
                    right -= 1
                else:
                    result.append([currentNum, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result 