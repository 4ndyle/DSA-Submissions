class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> values = new HashMap<>();
        int[] indexes = new int[2];

        for(int i = 0; i < nums.length; i++) {
            // calculate difference (target value)
            int difference = target - nums[i];

            // add value to hashmap if not equal to difference
            if(!values.containsKey(difference)) {
                values.put(nums[i], i);
            }
            else {
                // if it equals the difference
                indexes[0] = values.get(difference);
                indexes[1] = i;
            }
        }
        
        return indexes;
    }
}
