"""
Input:
    - str : s
Output:
    - bool : true if palindrome 
Constraints:
    - palindrome: reads same forwards and backwards (case insensitive and ignore non)
    - length of s: [1,1000]
    - values of s: Alphanumeric Characters (A-Z, a-z, 0-9)

Plan:
1. Create variables:
    - left = 0 
    - right = len(s) - 1
2. while left <= right:
        while s[left] is non-alphanumeric: 
            increment left
        while s[right] is non-alphanumeric:
            decrement right
        
        if s[left] != s[right]:
            return False
        
        increment left
        decrement right
3. Return true if all chars pass 
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
            