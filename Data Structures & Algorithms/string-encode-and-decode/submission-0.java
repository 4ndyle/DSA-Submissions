class Solution {

    public String encode(List<String> strs) {
        if(strs == null) {
            return "";
        }

        StringBuilder str = new StringBuilder();

        for(String currentStr : strs) {
            int strLength = currentStr.length();

            str.append(strLength + "#" + currentStr);
        }

        System.out.println(str.toString());

        return str.toString();
    } 

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();

        int numPointer = 0;

        while(numPointer < str.length()) {
            int poundIndex = str.indexOf('#',numPointer);

            // get the number before the pound (length)
            int wordLength = Integer.parseInt(str.substring(numPointer,poundIndex));

            // move pointer to beginnning of word
            numPointer = poundIndex + 1;
            String word = str.substring(numPointer, numPointer + wordLength);

            list.add(word);

            numPointer += wordLength;
        }

        return list;
    }
}
