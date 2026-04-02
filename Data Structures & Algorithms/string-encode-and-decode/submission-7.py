"""
Input: list (list of strings)
Output: list (list of strings after decoded)
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += f"{len(string)}#{string}"


        print(res)
        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            stringLength = int(s[i:j])

            start = j + 1
            j = start + stringLength

            substring = s[start:j]

            res.append(substring)
            i = j

        return res
