class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0

        while right < len(nums):

            # move left and right pointer when current element != val   
            if nums[left] == val:

                # move right pointer until an element not = val found 
                while right < len(nums) and nums[right] == val:
                    right += 1

                if right >= len(nums):
                    break

                # swap values and update pointers 
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                left += 1
                right += 1

        return left
