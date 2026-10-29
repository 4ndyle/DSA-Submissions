"""
Input:
    - List[str] : strs
Output:
    - List[List[str]] : group all anagrams into sublists 
Constraints:    
    - anagram: contains same characters as another string 
    - length of strs: [1,10000]
    - length of strs[i]: [0,100]
    - possible characters: lowercase english letters 

Example: 
{
    (index 0...26) : [group of anagrams]
}

key: tuple of length 26 where each index represents a alphabetical char
    find index of a char: 
        ord(currChar) - ord('a') = index
value: list of strings that are anagrams 
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for currString in strs:
            # create tuple representing letters/occurences of currString 
            charList = [0 for i in range(26)]

            for char in currString:
                charIndex = ord(char) - ord('a')
                charList[charIndex] += 1
            
            # convert list (mutable) to tuple (unmutable) and add to dict 
            tupleList = tuple(charList)

            if tupleList not in anagramDict:
                anagramDict[tupleList] = []

            anagramDict[tupleList].append(currString)

        return list(anagramDict.values())
            
