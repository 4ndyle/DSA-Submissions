class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        # initialize two pointers at start and end 
        left, right = 0, len(s) - 1

        s = s.lower()
        print(s)
        
        # while left is less than right
        while left < right:
            # skip non-alphanumeric characters
            while not s[left].isalnum() and left < right:
                left += 1 
            while not s[right].isalnum() and left < right:
                right -= 1

            print(f"checking {s[left]} + {left}")
            print(f"checking {s[right]} + {right}")
            # return false if character at indexes not equal
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1



        return True