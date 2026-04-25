public class Solution {
    public int LengthOfLongestSubstring(string s) {
        // create a variable to keep track of the window state and longest length
        HashSet<int> windowSymbols = new HashSet<int>();
        int longestLength = 0;

        // create a left pointer and right pointer for sliding window pattern 
        int left = 0;

        for (int right = 0; right < s.Length; right++) {
            char currSymbol = s[right];

            // update window when state is invalid 
            while (windowSymbols.Contains(currSymbol)) {
                windowSymbols.Remove(s[left]);
                left += 1;
            }

            // update the window state 
            windowSymbols.Add(currSymbol);

            // check if the current window length > previous window lengths 
            longestLength = Math.Max(longestLength, right - left + 1);
        }

        return longestLength;
    }
}
