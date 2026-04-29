public class Solution {
    public int MaxProfit(int[] prices) {
        int maxProfit = 0;

        // two pointers 
        int left = 0;

        for (int right = 0; right < prices.Length; right++) {
            // calcuate the proft for the current buy/sell prices 
            int currProfit = prices[right] - prices[left];
            maxProfit = Math.Max(maxProfit, currProfit);

            // if the current price is less than the left pointer (current buy), then update buy 
            if (prices[right] < prices[left]) {
                left = right;
            }
        }

        return maxProfit;
    }
}
