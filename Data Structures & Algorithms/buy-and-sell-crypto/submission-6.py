class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while(right < len(prices)):
            maxProfit = max(prices[right] - prices[left], maxProfit)
            if prices[right] < prices[left]:
                left = right
            else:
                right += 1

        print(prices)

        return maxProfit