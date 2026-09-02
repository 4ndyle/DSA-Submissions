class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)

        if k == len(cardPoints):
            return total

        maxScore = -float("inf")
        left = 0 
        windowLength = len(cardPoints) - k
        currWindowSum = 0

        for right in range(len(cardPoints)):
            currWindowSum += cardPoints[right]

            if right - left + 1 == windowLength:
                maxScore = max(total - currWindowSum, maxScore)
                currWindowSum -= cardPoints[left]
                left += 1

        return maxScore 