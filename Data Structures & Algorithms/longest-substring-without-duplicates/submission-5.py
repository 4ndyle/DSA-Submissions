"""
Input: string s 
Output: int (length of longest substring without duplicates)
Constraints: no duplicates 
Edge cases: 
    - empty string: Return 0 

Plan: 
Create a set to keep track of the current characters in the string
Create variable to keep track of the longest length 

Initialize two pointers, one left and one right

    Increment the right pointer when the current character is not in the set
    Otherwise, increment the left pointer and remove the character at the left pointer until
    there is no longer a duplicate 

return longest length variable  
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLength = 0
        left, right = 0, 0

        while right < len(s):

            if s[right] not in charSet:
                charSet.add(s[right])
                right += 1
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
                right += 1
                
            maxLength = max(maxLength, right-left)

        return maxLength
