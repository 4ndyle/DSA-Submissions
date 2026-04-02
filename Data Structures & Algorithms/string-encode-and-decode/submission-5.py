class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
    

        for s in strs:
            res += str(len(s)) + "#" + s

        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # increment the j pointer until we find the delimiter 
            while s[j] != '#':
                j += 1

            # find the length of the substring 
            strLen = int(s[i:j])

            # find the substring
            substring = s[j+1 : j+1+strLen]

            res.append(substring)
            i = j+1+strLen

        return res
