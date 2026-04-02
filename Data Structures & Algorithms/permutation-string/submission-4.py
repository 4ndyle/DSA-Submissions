class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = {}
        s2charMap = {}
        for char in s1:
            charMap[char] = charMap.get(char,0) + 1  
            s2charMap[char] = s2charMap.get(char,0)
        
        print(charMap)
        print(s2charMap)

        left = 0

        for right in range(len(s2)):

            if s2[left] not in charMap or right-left+1 > len(s1):
                if s2[left] in s2charMap:
                    s2charMap[s2[left]] -= 1
                left += 1

            if s2[right] in s2charMap:
                s2charMap[s2[right]] += 1

                if charMap == s2charMap and right-left+1 == len(s1):
                    return True

            right += 1

        print(s2charMap)


        return False