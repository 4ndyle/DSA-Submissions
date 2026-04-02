class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            countList = [0] * 26 

            for char in string:
                countList[ord(char) - ord("a")] += 1

            res[tuple(countList)].append(string)

        return res.values()
