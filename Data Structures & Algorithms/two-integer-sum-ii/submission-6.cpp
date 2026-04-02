class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int start = 0;
        int end = numbers.size() - 1;
        int currentSum = 0;
        cout << currentSum;

        while (start < end) {
            currentSum = numbers[start] + numbers[end];
            
            if (currentSum > target) {
                end--;
            }
            else if (currentSum < target) {
                start++;
            }
            else {
                break;
            }
        }

        return {start + 1, end + 1};
    }
};
