class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(openCount, closeCount):
            # base case
            if openCount == closeCount == n:
                result.append("".join(stack))
                return

            # add oepning bracket
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()

            # add closing bracket
            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(0, 0)
        return result