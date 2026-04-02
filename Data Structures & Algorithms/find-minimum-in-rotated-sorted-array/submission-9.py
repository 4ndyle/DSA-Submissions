class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        res = float('inf')

        while start <= end:
            mid = (start + end) // 2

            # search left when nums[end] > nums[mid]
            if nums[end] >= nums[mid]:
                end = mid - 1
            elif nums[start] <= nums[mid]:
                start = mid + 1
            res = min(nums[mid],res)

        return res

