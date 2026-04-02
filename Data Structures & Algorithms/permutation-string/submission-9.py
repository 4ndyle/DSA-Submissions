"""
Input: 
    - string : s1
    - string : s2
Output: 
    - boolean : represents whether or not s2 contains a permutation of s1
Constraints:
    - both strings contain only lowercase characters 
    - 1 <= s1.length, s2.length <= 1000

Plan: 
1. Use a dict to get the frequency count of s1. 
2. Create a dict to get frequency count for s2 and iterate through the s2 string and update the 
dict
    - if the dict of s1 and s2 are equal, return true 
3. If we go through the whole s2 string without finding a match, return False 

Psuedo Code:
s1CharCount = {}

for char in s1:
    s1CharCount[char] = s1CharCount.get(char, 0) + 1

s2CharCount = {}
left = 0 
right = len(s1) - 1

get the current count of the window 
for i in range(right):
    s2CharCount[s2[i]] = s2CharCount.get(s2[i], 0) + 1

while right < len(s2):
    if s1CharCount == s2CharCount:
        return True

    Shrink the left side of window 
    s2CharCount[left] -= 1
    left += 1

    Expand the right side of window 
    s2CharCount[right] = s2CharCount.get(s2[right], 0) + 1

return False 

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # get the frequency count for chars in s1
        s1CharCount = {}

        for char in s1:
            s1CharCount[char] = s1CharCount.get(char, 0) + 1

        # get the frequency count for chars in s2
        s2CharCount = {}
        left = 0
        right = len(s1) - 1

        for i in range(len(s1)):
            s2CharCount[s2[i]] = s2CharCount.get(s2[i], 0) + 1
        
        if s1CharCount == s2CharCount:
            return True 

        print(s1CharCount)
        print(s2CharCount)
        print()

        # move the fixed sliding window through the string and check if a permutation exists 
        while right < len(s2) - 1:
            print(f"checking window {s2[left:right+1]}")
            print(s2CharCount)
            print()

            # shrink the left side of window 
            s2CharCount[s2[left]] -= 1

            if s2CharCount[s2[left]] == 0:
                del s2CharCount[s2[left]]

            left += 1

            # expand the right side of window 
            right += 1
            s2CharCount[s2[right]] = s2CharCount.get(s2[right], 0) + 1

            if s1CharCount == s2CharCount:
                return True 


        return False 