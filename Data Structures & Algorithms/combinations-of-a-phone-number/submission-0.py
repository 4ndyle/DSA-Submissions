class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create hash map of mappings 
        numberToLetters = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d', 'e', 'f'],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        # go through the string and add each possible combination to list 
        totalCombinations = []

        def dfsHelper(currString, combination):
            # base case 
            if currString == "":
                totalCombinations.append(combination)
                return

            currDigit = currString[0]

            # process current digit and add each letter of current digit to combination 
            for currLetter in numberToLetters[currDigit]:
                combination += currLetter
                dfsHelper(currString[1:], combination)
                combination = combination[:-1]
        
        dfsHelper(digits, "")
        return [] if digits == "" else totalCombinations