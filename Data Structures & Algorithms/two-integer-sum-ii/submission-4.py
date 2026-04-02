class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers ascending order
        # return [index1, index2] (1-indexed)

        start = 0
        end = len(numbers) - 1
        currentSum = 0

        while start < end:
            currentSum = numbers[start] + numbers[end]

            # move right pointer when the sum is greater than target
            # move left pointer when the sum is less than target
            if currentSum > target:
                end -= 1
            elif currentSum < target:
                start += 1
            else:
                break
                
        return [start + 1, end + 1]

            