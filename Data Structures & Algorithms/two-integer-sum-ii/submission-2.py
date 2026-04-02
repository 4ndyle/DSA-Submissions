class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while(left < right):
            sum = numbers[left] + numbers[right]
            print(sum)

            # increment left pointer if value is less than target
            if sum < target:
                left += 1

            # increment right pointer if value is greater than target
            elif sum > target: 
                right -= 1

            else:
                return [left+1,right+1]

        return []