"""
Input: 
    - string : s (only contains upppercase english characters)
    - int : k 
Output:
    - int : length of the longest substring containing only one distinct char
Constraints
    - only contains uppercase english characters 
    - 1 <= s.length <= 1000
    - 0 <= k <= s.length
Edge Cases:
    - "XYZ", k = 3 ->  3
    - string, k = 0 -> returning substring with longest distinct characters

Plan: Use a sliding window to got through the string. Expand the right side of the window 
and use a dict to keep track of the frequency of each character. When the window has k number of 
other characters that are not the most commonly occuring, we can replace those characters 
and record the length of the substring. 

Psuedo Code:
left = 0
charCount = {}
maxLength = 0

for right in range(len(s)):
    charCount[s[right]] = charCount.get(s[right], 0) + 1

    numReplacements is length of the string - most frequent character 

    while numReplacements > k:
        decrement the count of the current char at left
        increment the left pointer

    update the maxLength variable and check if the current window length
    is greater than the max length or not 

return maxLength 
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        charCount = {}
        maxLength = 0

        for right in range(len(s)):
            charCount[s[right]] = charCount.get(s[right], 0) + 1

            # number of replacements = (right - left + 1) - max(charCount frequencies)

            while (right - left + 1) - max(charCount.values()) > k:
                charCount[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength


