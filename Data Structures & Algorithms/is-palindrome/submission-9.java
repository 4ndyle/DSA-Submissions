class Solution {
    public boolean isPalindrome(String s) {
        String regex = "[?*&#!,`~'.:; ]";
        String newString = s.replaceAll(regex, "").toLowerCase();
        System.out.print(newString);

        // two pointers at beginning and end of string
        int i = 0;
        int j = newString.length() - 1;

        while(i <= j) {
            if(newString.charAt(i) != newString.charAt(j)) {
                return false;
            }
            else {
                i++;
                j--;
            }
        }

        return true;
    }
}
