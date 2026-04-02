class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create dict for both strings
        sDict = {}
        tDict = {}

        # map each character in the string to their frequencies in the dict
        for char in s:
            sDict[char] = sDict.get(char, 0) + 1

        for char in t:
            tDict[char] = tDict.get(char, 0) + 1

        return sDict == tDict
