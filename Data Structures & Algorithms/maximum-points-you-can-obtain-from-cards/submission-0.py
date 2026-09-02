class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)

        if k == len(cardPoints):
            return total

        minWindowSum = float("inf")
        maxScore = 0 
        left = 0 
        currWindowSum = sum(cardPoints[left : len(cardPoints) - k - 1])

        for right in range(len(cardPoints) - k - 1, len(cardPoints)):
            currWindowSum += cardPoints[right]

            if currWindowSum  < minWindowSum:
                minWindowSum = currWindowSum
                maxScore = total - currWindowSum

            currWindowSum -= cardPoints[left]
            left += 1

        return maxScore 