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
        maxLength = 0 
        windowSet = set()
        left = 0

        for right in range(len(s)):
            # shrink window if new character is in current window 
            while s[right] in windowSet:
                windowSet.remove(s[left])
                left += 1

            # update window state 
            windowSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength