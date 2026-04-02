"""
Input: 
    - string : s
Output: 
    - int :length of the longest substring without duplicates 
Constraints:
    - 0 <= s.length <= 1000
    - s may consist of printable ASCII Characters 
Edge Cases:
    - "" -> return 0

Plan: Use a sliding window and a set to keep track of the current characters
in the window of strings. Move the right pointer and when there is a duplicate,
move the left pointer until there are no duplicates. 

Psuedo Code:
windowChars = set()
left = 0
maxLength = 0

for right in range(len(s)):

    if the current character at the right pointer is in the set:
        
        while the currentChar is in the set:
            remove the current char at the left pointer
            increment the left pointer

    add the current character into the set
    update the maxLength variable to record the max length (window length can be right - left or set size)

return maxLength


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowChars = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            currentChar = s[right]
            print(f"checking current char {currentChar} for string {s[left:right]}")
            if currentChar in windowChars:
                while currentChar in windowChars:
                    windowChars.remove(s[left])
                    left += 1
                print(f"updated string to {s[left:right]}")

            windowChars.add(currentChar)
            maxLength = max(right - left + 1, maxLength)
            print()

        return maxLength

    