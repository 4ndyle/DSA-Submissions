class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        res = nums[0]

        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break

            mid = (start + end) // 2
            res = min(res, nums[mid])
            # search right
            if nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return res

