class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # target is found 
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # mid is in the left section of numbers
                if target > nums[mid] or target < nums[left]:
                    # search right
                    left = mid + 1
                else:
                    # search left
                    right = mid - 1
            else:
                # mid in right section
                if target > nums[right] or target < nums[mid]:
                    # search left
                    right = mid - 1
                else:
                    left = mid + 1

        return -1