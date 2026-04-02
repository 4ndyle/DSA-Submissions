class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # add character to both maps 
        charMap = {}
        s2charMap = {}
        for char in s1:
            charMap[char] = charMap.get(char,0) + 1  
            s2charMap[char] = s2charMap.get(char,0)
        

        left = 0
        # sliding window
        for right in range(len(s2)):
            # move left pointer when character is not in s2 or if length is surpassed
            if s2[left] not in charMap or right-left+1 > len(s1):
                # decremenet character count if in s2 map
                if s2[left] in s2charMap:
                    s2charMap[s2[left]] -= 1
                left += 1

            # check if substring is found yet
            if s2[right] in s2charMap:
                s2charMap[s2[right]] += 1

                if charMap == s2charMap and right-left+1 == len(s1):
                    return True

        return False