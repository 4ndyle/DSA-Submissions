class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string
        sortedStrings = []
        for string in strs:
            sortedStrings.append(''.join(sorted(string)))

        print(sortedStrings)

        # hashmap with key as sorted string and val as sublists
        groups = {}
        for i in range(len(strs)):
            string = sortedStrings[i]

            if string in groups:
                groups[string].append(strs[i])
            else:
                groups[string] = [strs[i]]

        result = []
        for val in groups.values():
            result.append(val)

        return result
