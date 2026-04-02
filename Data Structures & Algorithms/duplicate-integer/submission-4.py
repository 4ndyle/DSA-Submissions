"""
Input: 
    - List[int] : nums
Output
    - bool : represent if there is duplicate or not 
Constraints:
    - input arrays are not sorted 
    - neg, pos, or zero
Edge Cases:
    - [] -> False 

Plan: 
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()

        for num in nums:
            if num not in seenNums:
                seenNums.add(num)
            else:
                return True

        return False