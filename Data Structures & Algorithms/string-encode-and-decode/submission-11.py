"""
Machine 1: 
1. Get the string 
2. pass it into the encode function 
3. output the encoded string 

Machine 2:
1. Receive the encoded string
2. pass the encoded into the decode function 
3. return the original string


Constraints:
    - strs[i] contains any possible chars out of the 256 valid ascii characters 
    - 0 <= strs.length < 100
    - 0 <= strs[i].length < 100

Example:
["Hello","Wo#rld","Andy"]

Encode(str) -> 
    - #5Hello#6Wo#rld#4Andy
"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        
        # split each string using deliminator and length of string 
        for string in strs:
            res += f"{len(string)}" + "#" + string

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        # process the string by each deliminator 
        i = 0

        while i < len(s):
            j = i

            # increment the j pointer until we find the deliminator 
            while s[j] != "#":
                j += 1
            
            strLen = int(s[i:j])

            # find the substring
            substring = s[j+1 : j + 1 + strLen]
            res.append(substring)

            i = j + 1 + strLen

        print(res)
        return res 

