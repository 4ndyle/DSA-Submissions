class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            # add char to map if not existing
            charMap[s[right]] = charMap.get(s[right],0) + 1
            mostOccuring = max(charMap.values())

            # not valid, move left pointer if number of chars to replace is greater than k
            length = right - left + 1
            while (right - left + 1) - mostOccuring > k:
                # remove char at left pointer and move pointer
                charMap[s[left]] -= 1
                left += 1
                mostOccuring = max(charMap.values())

            result = max(result, right - left + 1)

        return result

