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
        # Create a variable to keep track of the longest length (int)
        windowSymbols = set()
        longestLength = 0

        # Create left pointer and right pointer for sliding window 
        left = 0

        for right in range(len(s)):
            currSymbol = s[right]

            # shrink the window when state is invalid 
            while currSymbol in windowSymbols:
                windowSymbols.remove(s[left])
                left += 1

            # update the window with the new character 
            windowSymbols.add(currSymbol)

            # check if the current window length > previous lengths 
            longestLength = max(longestLength, right - left + 1)

        return longestLength