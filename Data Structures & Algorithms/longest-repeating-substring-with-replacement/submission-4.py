"""
Input:
    - str : s
    - int : k
Output: 
    - int : length of the longest substring after at most k replacements 

Example 2: 
Input: s = "AAABABB"

Notes: 
1. Find the most frequently occuring character in our substring 
2. number of non-distinct characters in substring = len(substring) - number of occurences (most frequent character in substring)

Plan:
1. Use a dict to keep track of the occurences of the characters 
2. Use a variable to keep track of the most frequently occuring character 
3. Use a sliding window to iterate through the string 
    - Shrink the window from the left side when there num of non-distinct chars > k

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        charCount = {}

        # sliding window 
        left = 0

        for right in range(len(s)):
            currChar = s[right]
            charCount[currChar] = charCount.get(currChar, 0) + 1

            # shrink window when state is invalid 
            while (right - left + 1) - max(charCount.values()) > k: 
                charCount[s[left]] -= 1
                left += 1

            # compare the current length of window with previous lengths
            maxLength = max(maxLength, right - left + 1)

        return maxLength


        
