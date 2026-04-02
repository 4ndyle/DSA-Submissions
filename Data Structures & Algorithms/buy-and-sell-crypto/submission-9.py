class Solution:
    '''
    goal: maximize the profit
    profit = selling price - buying price 

    one pointer represents the buying price 
    one pointer represents the selling price 
    '''
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):

            # set left pointer to price at right pointer if less than current price in left pointer
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            
            # move right pointer to next value 
            right += 1
        
        return maxProfit


