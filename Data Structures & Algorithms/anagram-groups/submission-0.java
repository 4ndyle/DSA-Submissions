class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();

        for(String currentString: strs) {
            char[] charArr = currentString.toCharArray();
            Arrays.sort(charArr);
            
            String sortedString = new String(charArr);

            // create new list if string does not exist
            result.putIfAbsent(sortedString, new ArrayList<>());

            // add currentString to list of anagrams group 
            List<String> list = result.get(sortedString);
            list.add(currentString);
        }

        return new ArrayList<>(result.values());
    }
}
