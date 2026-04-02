"""
Input: list (list of strings)
Output: list (contain list of lists where each list is a anagram group)
Constraints:
    - each list is going to be a anagram group where each string
    has to be a anagram of all strings in that group
Edge Cases:
    - list of one string -> [[one string]]
    - list of empty string -> [[""]]

Plan: Use a dict to store the char count of the various strings as the key. If
the character count already exists, then we add it to the values of that key.
Key: (26 indexes where each indice is a letter a-z)
Value: [list of strings where they have the same letters]

Initialize a dict with default a default value of a list

for string in strs:
    charListCount = [0] * 26

    for char in string:
        charIndex = ord(char) - ord("a")

        increment the index of the charIndex in our list frequency

    if the char frequency already exists, append it to the list
    otherwise, create a new key and append it to the value list

return dict values as a list
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroupsDict = defaultdict(list)

        for string in strs:
            charListCount = [0] * 26

            for char in string:
                charIndex = ord(char) - ord("a")
                charListCount[charIndex] += 1

            anagramGroupsDict[tuple(charListCount)].append(string)

        return list(anagramGroupsDict.values())


