"""
Input:
    - str : s 
Output:
    - int : longest substring length without duplicate characters 

Constraints:
    - length of string : 0 <= s.length <= 1000
    - printable ASCII characters 

Plan: Use a sliding window to iterate through the array and keep track of the length 
of the longest substring using a variable 

Example 1:
Input: s = "zxyzxyz"


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a variable to keep track of the max length of the substring (without duplicates)
        longestSubstringLen = 0

        # Use as sliding window to find substrings without duplicates 
        substringChars = set()
        left = 0

        for right in range(len(s)):
            currChar = s[right]

            # ensure window doesn't contain duplicates (shrink from left side)
            while currChar in substringChars:
                substringChars.remove(s[left])
                left += 1
            
            # add the current character to set 
            substringChars.add(currChar)

            # find the current length of window and update longest substring 
            longestSubstringLen = max(longestSubstringLen, right - left + 1)
        
        return longestSubstringLen

"""
Time - O(N) : iterating through the array once 
Space - O(N) : worse case where we get a unique string 
"""

