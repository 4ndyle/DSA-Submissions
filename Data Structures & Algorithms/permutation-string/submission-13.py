class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        # get freq count of s1
        s1Freq = {}

        for char in s1:
            s1Freq[char] = s1Freq.get(char, 0) + 1

        # Use a sliding window to scan through the string and check frequencies
        # length of sliding window = len(s1)

        left = 0
        right = 0
        s2Freq = {}

        # expand window until length of s1 is reached
        while right < len(s1):
            currChar = s2[right]
            s2Freq[currChar] = s2Freq.get(currChar, 0) + 1

            right += 1

        if s1Freq == s2Freq:
            return True

        # move the sliding window until the end s2 and check frequencies 
        while right < len(s2):
            # expand window on right side
            s2Freq[s2[right]] = s2Freq.get(s2[right], 0) + 1
            right += 1

            # shrink window from left side
            s2Freq[s2[left]] -= 1

            if s2Freq[s2[left]] == 0:
                del s2Freq[s2[left]]
                
            left += 1

            if s1Freq == s2Freq:
                return True

        return False 