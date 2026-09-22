"""
Encode
Input:
    - List[str] : strs
Output:
    - str : encoded string 

Decode 
Input:
    - str : encoded_string
Output:
    - List[str] : list of decoded strings (original input to encode)

length of strs: [0,100]
values of strs: any possible character out of 256 ASCII charactrs
length of strs[i]: [0,200]

Plan: Encode the string using a character to split the string and string's length
Input: strs = ["Hello","#4","World"]
Output: "5#Hello2#4#5#World"

Input: strs = ["Hello World", "Hi"]
Output: "11#Hello World2#Hi"

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += f"{len(string)}#{string}"
        
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            # find the string length
            numberString = ""

            while s[i] != '#':
                numberString += s[i]
                i += 1

            stringLength = int(numberString)
            i += 1

            # parse the string and add to the result
            currString = ""

            for _ in range(stringLength):
                currString += s[i]
                i += 1
            
            result.append(currString)

        return result
