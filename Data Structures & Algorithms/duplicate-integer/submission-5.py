class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()

        for num in nums:
            # if we have seen the number, return False 
            if num in seenNums:
                return True

            # otherwise, add the number to the set 
            else:
                seenNums.add(num)

        return False