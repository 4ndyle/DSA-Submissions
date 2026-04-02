class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> numbers;

        for(int currentNum : nums) {
            if(numbers.find(currentNum) != numbers.end()) {
                return true;
            }
            else {
                numbers.insert(currentNum);
            }
        }

        return false;
    }
};
