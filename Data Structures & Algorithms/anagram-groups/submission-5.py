class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: char count represented as a tuple
        # value: list [] that contains each group
        anagramGroups = defaultdict(list)

        for string in strs:
            charCountList = [0] * 26

            for char in string:
                charCountList[ord(char) - ord("a")] += 1
            
            anagramGroups[tuple(charCountList)].append(string)
            

        return list(anagramGroups.values())
            
        