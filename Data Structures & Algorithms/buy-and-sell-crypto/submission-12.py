"""
Input:
    - List<int> : prices 
Output:
    - int : max profit 
Constraints:
    - prices length: [1,100]
    - prices[i]: [0,100]

Plan: Use two points to scan through days and calculate the proft for each iteration 
    - left pointer: lowest price to buy 
    - right pointer: current price that we are at 
    - compare the profit at each iteration and store the max 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 

        # two pointer 
        left = 0

        for right in range(len(prices)): 
            # calculate the max profit of the current iteration
            currProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit, currProfit)

            # if the current number is less than left pointer number, update left 
            if prices[right] < prices[left]:
                left = right 

        return maxProfit 
                