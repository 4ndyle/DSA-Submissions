class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        for char in s:
            sCount[char] = sCount.get(char, 0) + 1

        for char in t:
            tCount[char] = tCount.get(char, 0) + 1

        return sCount == tCount