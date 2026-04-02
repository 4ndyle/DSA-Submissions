class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        // create hashmap for both strings
        Map<Character, Integer> smap = new HashMap<>();
        Map<Character, Integer> tmap = new HashMap<>();

        for(int i = 0; i < s.length(); i++) {
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);

            // add char values to s map
            smap.putIfAbsent(sChar, 0);
            smap.replace(sChar, smap.get(sChar)+1);

            // add char values to t map
            tmap.putIfAbsent(tChar, 0);
            tmap.replace(tChar, tmap.get(tChar)+1);
        }

        for(char letter : smap.keySet()) {
            if(smap.get(letter) != tmap.get(letter)) {
                return false;
            }
        }

        return true;
    }
}
