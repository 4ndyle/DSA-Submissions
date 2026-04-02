class Solution {
    public int maxProfit(int[] prices) {
        // base case
        if (prices == null || prices.length < 2) {
            return 0;
        }

        int minPrice = prices[0];  // Track the minimum price encountered
        int maxProfit = 0;         // Track the maximum profit possible
        
        for (int i = 1; i < prices.length; i++) {
            // If current price is lower than the minimum, update minPrice
            if (prices[i] < minPrice) {
                minPrice = prices[i];
                System.out.println("New min price: " + minPrice);
            } else {
                // Otherwise, calculate profit and update maxProfit if it's higher
                int profit = prices[i] - minPrice;
                if (profit > maxProfit) {
                    maxProfit = profit;
                    System.out.println("New max profit: " + maxProfit);
                }
            }
        }
        
        return maxProfit;
    }
}
