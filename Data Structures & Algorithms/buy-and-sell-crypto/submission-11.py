"""
Input: 
    - List[int] : prices where prices[i] = stock price on the ith day 
Output: 
    - int : max profit you can achieve 
    - lowest profit = 0 

Example 1:
prices = [10,1,5,6,7,1,0,2,3]

Plan: Use two pointers to keep track of the buy stock and sell stock while calculating their 
difference at each iteration. Keep track of the max profit in a variable 
    - left pointer : point to the lowest stock price 
    - right pointer : stock prices we iterate through 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create a variable for keeping track of the max profit 
        maxProfit = 0

        # create pointers for our list 
        left = 0
        
        for right in range(len(prices)):
            # encounter a lower price than buy price (left pointer), update our buying target
            if prices[left] > prices[right]:
                left = right

            # calculate profit and update max profit 
            currProfit = prices[right] - prices[left]   
            maxProfit = max(currProfit, maxProfit)

        return maxProfit

"""
prices = [10,1,5,6,7,1,0,2,3]
"""