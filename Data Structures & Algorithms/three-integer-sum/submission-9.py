class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a variable to store triplets and sort the nums list 
        triplets = []
        nums.sort()

        # iterate throughe each num and use two pointers to find two other numbers that sum up to 0
        for i in range(len(nums)):
            # skip duplicate numbers 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # find two numbers other numbers with the current number that sum to 0
            currNum = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right: 
                currSum = currNum + nums[left] + nums[right]
                print(f"sum = {currSum}")

                if currSum < 0:
                    print("increasing sum")
                    left += 1
                elif currSum > 0:
                    print("decreasing sum")
                    right -= 1
                else:
                    triplets.append([currNum, nums[left], nums[right]])
                    print("sum = 0")

                    # move onto next number 
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return triplets 


        