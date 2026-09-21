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
2. For currString in strs:
        sortedString = currString.sort()

        if sortedString in dict:
            add currString to stringGroups[sortedString]
        else:
            stringGroups[sortedString] = []
            add currString to stringGroups[sortedString]
3. Convert dict to list of groups
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringGroups = {}

        for currString in strs:
            sortedString = "".join(sorted(currString))

            if sortedString not in stringGroups:
                stringGroups[sortedString] = []
                
            stringGroups[sortedString].append(currString)

        # print(list(stringGroups.values()))
        return list(stringGroups.values())
