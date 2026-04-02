"""
Input:
    - list[str] : strs
Output:
    - List[List[str]] : each sublist is a group of anagrams 

Anagram - string that contains the same characters as another string in any order 

Approaches: 
1. Sort each string and compare each string. If they match add them into their respective group
using a dictionary
2. Create a array of length 26 where each index is the char count. Calculate the ascii index
of each string and update the count in the array. 
    Dict: tuple -> [str]

# b : 76
# a : 75
# b - a = 1 where 1 is the index of character b

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # crete a dict to represent groups 
        anagramGroups = {}

        # loop through each string and get its character count 
        for string in strs:

            # create array of length 26 representing char count 
            charCountArr = [0] * 26

            # loop through each character and update character count in arr
            for char in string:
                charIndex = ord(char) - ord("a")

                charCountArr[charIndex] += 1

            # update anagram groups 
            charCount = tuple(charCountArr)
            
            if charCount not in anagramGroups:
                anagramGroups[charCount] = []

            anagramGroups[charCount].append(string)

        return list(anagramGroups.values())




