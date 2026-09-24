class Solution:
    def minOperations(self, s: str) -> int:
        firstPassChanges = self.totalOperations(s, '0')
        secondPassChanges = self.totalOperations(s, '1')

        return min(firstPassChanges, secondPassChanges)

    def totalOperations(self, s, expectedBinary):
        changes = 0 

        for char in s:
            if char != expectedBinary:
                changes += 1
            
            # update expected binary
            if expectedBinary == '0':
                expectedBinary = '1'
            else:
                expectedBinary = '0'

        return changes