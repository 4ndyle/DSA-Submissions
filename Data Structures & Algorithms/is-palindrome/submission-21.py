class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        left = 0
        right = len(s) - 1

        while left < right: 
            # skip non-alpha-numeric characters 
            while left < right and not s[left].isalnum():
                print("left is not a alpha numeric char")
                left += 1
            while left < right and not s[right].isalnum():
                print("right is not a alpha numeric char")
                right -= 1

            # check current character
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True