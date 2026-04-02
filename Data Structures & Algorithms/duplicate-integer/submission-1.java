class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numsList = new HashSet<Integer>();

        for(int i = 0; i < nums.length; i++) {
            if(numsList.contains(nums[i])) {
                return true;
            }
            else {
                numsList.add(nums[i]);
            }
        }
        return false;
    }
}
