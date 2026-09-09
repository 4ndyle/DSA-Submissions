
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


        
