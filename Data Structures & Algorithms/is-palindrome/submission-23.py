"""
Input:
    - str : s
Output:
    - bool : true if it is a palindrome 

Palindrome:
    - string that reads the same forward and backward 
    - case insensitive and ignores non-alphanumeric characters

Constraints:
    - string length : 1 <= s.length <= 1000
    - s is made up of only printable ASCII characters
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # create a pointer at the start and end of the string
        left = 0
        right = len(s) - 1

        # move pointers towards middle of string until they cross or are not equal
        while left < right:
            # update pointers when they are not alphanumeric
            while not s[left].isalnum() and left < right:
                print(f"{s[left]} is not alnum, move left")
                left += 1
            
            while not s[right].isalnum() and left < right:
                print(f"{s[right]} is not alnum, move right")
                right -= 1

            # check if character at left and right equal
            if s[left] != s[right]:
                return False

            # update pointers to move towards middle
            left += 1
            right -=1

        return True