"""
left = 0
right = 1
maxProfit = 0

while right < len(prices):
    currentProfit = prices[right] - prices[left]

    maxProfit = max(maxProfit, currentProfit)

    if prices[right] < prices[left]:
        left = right

    right += 1
"""

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            currentProfit = prices[right] - prices[left]

            maxProfit = max(maxProfit, currentProfit)

            if prices[right] < prices[left]:
                left = right

            right += 1

        return maxProfit



