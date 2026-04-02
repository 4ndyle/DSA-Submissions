class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # create left and right pointers at start and end
        left = 0
        right = len(numbers) - 1

        while(left < right):
            sum = numbers[left] + numbers[right]

            # non-decreasing order
            # decrement right pointer if target is less than sum
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1,right+1]

        return [] 

