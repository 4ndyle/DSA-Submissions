"""
Input:
    - List[str] : strs
Output:
    - List[List[str]] : anagrams grouped into sublists
Constraints:
    - lenght of str: [1,10000]
    - lenght of str[i]: [1,100]
    - values of str[i]: lowercase english characters

Plan:
1. Create a dict to keep track of groups
    - stringGroups = {}
2. for currString in strs:
        lettersList = [0] * 26

        for char in currString:
            lettersList += ord(char) - ord('a')

        stringGroups[tuple(lettersList)].append(currString)
3. Return list(stringGroups.values())
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringGroups = {}

        for currString in strs:
            lettersList = [0] * 26

            for char in currString:
                lettersList[ord(char) - ord('a')] += 1
            
            lettersTuple = tuple(lettersList)
            if lettersTuple not in stringGroups:
                stringGroups[lettersTuple] = []

            stringGroups[lettersTuple].append(currString)

        return list(stringGroups.values())
            
