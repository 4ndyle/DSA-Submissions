class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // map each num to their frequencies in a hashmap (key - num : value - frequency)
        HashMap<Integer, Integer> numbers = new HashMap<>();

        for(int currentNum : nums) {
            numbers.putIfAbsent(currentNum, 0);
            numbers.put(currentNum, numbers.get(currentNum)+1);
        }

        // add mapped key and value into array list to sort in descending order
        List<int[]> arr = new ArrayList<>();

        for(Map.Entry<Integer, Integer> currentEntry : numbers.entrySet()) {
            arr.add(new int[] {currentEntry.getKey(), currentEntry.getValue()});
        }
        arr.sort((a,b) -> b[1] - a[1]);

        // add top k values to array and return 
        int[] topK = new int[k];
        for(int i = 0; i < k; i++) {
            int[] numWithKey = arr.get(i);
            topK[i] = numWithKey[0];
        }

        return topK;
    }
}
