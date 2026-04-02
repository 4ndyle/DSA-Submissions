"""
Input: 
    - List[int] : nums
Output: 
    - List[int] : of length 2n and concatenation of two nums arrays 
Constraints:
    - length : 1 <= nums.length <= 1000
    - range of values : 1 <= nums[i] <= 1000
Edge Cases:
    - [1] -> [1,1]

Plan: 
1. Create a empty array to hold our result 
2. Loop through the input nums 2 times to add each element into the array 
3. Return result array
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(2):
            for num in nums:
                result.append(num)

        return result