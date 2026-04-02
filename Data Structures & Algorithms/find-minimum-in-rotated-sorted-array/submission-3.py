class Solution:
    def findMin(self, nums: List[int]) -> int:
        # case when rotatation results in orginal
        if nums[0] <= nums[len(nums) - 1]:
            return nums[0]

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

