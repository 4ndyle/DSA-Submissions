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
        longestSubstringLen = 0

        # Create a dict to keep track of the frequencies of the characters 
        charFreq = {}

        # Create a variable to keep track of the most frequent character in substring 
        maxOccurences = 0
        mostFreqChar = ""

        # Use a sliding window to iterate through s 
        left = 0

        for right in range(len(s)):
            currChar = s[right]

            # update char frequency and most frequent character 
            charFreq[currChar] = charFreq.get(currChar, 0) + 1

            if charFreq[currChar] >= maxOccurences:
                maxOccurences = charFreq[currChar]
                mostFreqChar = currChar

            # calculate the number of possible replacements in substring s 
            while (right - left + 1) - maxOccurences > k:
                charFreq[s[left]] -= 1
                left += 1

            numOfReplacements = (right - left + 1) - maxOccurences

            # update the length of longest substring
            if numOfReplacements <= k:
                longestSubstringLen = max(right - left + 1, longestSubstringLen)

        return longestSubstringLen

        
