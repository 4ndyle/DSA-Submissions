class Solution {
    public boolean isAnagram(String s, String t) {
        // edge case
        if(s.length() != t.length()) {
            return false;
        }

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        Arrays.sort(sArr);
        Arrays.sort(tArr);

        String newS = new String(sArr);
        String newT = new String(tArr);

        System.out.println(sArr);
        System.out.println(tArr);

        if(newS.equals(newT)) {
            return true;
        }
        return false;
    }
}
