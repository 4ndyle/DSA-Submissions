class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        left = 0
        result = 0

        for right in range(len(s)):
            currentChar = s[right]

            # remove duplicates from set and substring
            while currentChar in charSet:
                charSet.remove(s[left])
                left += 1


            charSet.add(currentChar)
            result = max(result, right - left + 1)

        return result