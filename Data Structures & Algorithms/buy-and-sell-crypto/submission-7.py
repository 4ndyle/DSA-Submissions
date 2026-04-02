class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while(right < len(prices)):
            maxProfit = max(prices[right] - prices[left], maxProfit)

            # move left pointer to right if lower than left's value
            if prices[right] < prices[left]:
                left = right
            else:
                right += 1

        return maxProfit