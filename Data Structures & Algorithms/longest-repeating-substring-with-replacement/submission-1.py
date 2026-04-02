'''
Input: string (consisting of upper chars), integer (choose up to k characters of string and replace with any other char)
Output: integer (length of the longest substring containing one distinct character)
Constraints:
    - consisting of only uppercase characters
    - choose up to k characters to replace
    - return lenght of longest substring containing one distinct character
Edge Cases: 
    - Empty String: return 0
    - String of all same characters: return length of the string 

Plan: Use sliding window approach and shrink the window when the number of replacements exceeds k
Initialize left and right pointers
Initialize a dict to keep track of frequency
Initialize varaible to keep track of longest length

while right < len(s):
    add the count of the current character to the frequency dict
    totalReplacements = length of substring (right - left) - most frequent character count 

    while totalReplacements > k:
        dict[s[left]] = dict[s[left]] - 1
        left += 1

    longestLength = max(longestLength, right-left)
    right += 1

return longestLength

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0   
        frequency = {}
        maxLength = 0

        while right < len(s):
            frequency[s[right]] = frequency.get(s[right], 0) + 1

            while (right-left+1) - max(frequency.values()) > k:
                frequency[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right-left+1)
            right += 1

        return maxLength

    