class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1


        while start <= end:
            middle = (end+start) // 2
            if target == nums[middle]:
                return middle
            elif(target < nums[middle]):
                # search left half
                end = middle - 1
            else:
                # search right half
                start = middle + 1

        return -1

