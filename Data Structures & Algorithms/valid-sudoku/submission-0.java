class Solution {
    public boolean isValidSudoku(char[][] board) {
        // check each row for digits
        for(int row = 0; row < 9; row++) {
            HashSet<Character> digits = new HashSet<>();

            for(int col = 0; col < 9; col++) {
                char currentChar = board[row][col];

                if(currentChar == '.') {
                    continue;
                }
                else if(digits.contains(currentChar)) {
                    return false;
                }
                else {
                    digits.add(currentChar);
                }
            }
        }

        // check each column for the digits 
        for(int col = 0; col < 9; col++) {
            HashSet<Character> digits = new HashSet<>();

            for(int row = 0; row < 9; row++) {
                char currentChar = board[row][col];

                if(currentChar == '.') {
                    continue;
                }
                else if(digits.contains(currentChar)) {
                    return false;
                }
                else {
                    digits.add(currentChar);
                }
            }
        }

        // check each row and col of 3x3 sub boxes (total of 9)
        for(int box = 0; box < 9; box++) {
            HashSet<Character> digits = new HashSet<>();

            // check each 3x3 sub box
            for(int i = 0; i < 3; i++) {
                for(int j = 0; j < 3; j++) {
                    int row = (box / 3) * 3 + i;
                    int col = (box % 3) * 3 + j;
 
                    char currentChar = board[row][col];

                    if(currentChar == '.') {
                        continue;
                    }
                    else if(digits.contains(currentChar)) {
                        return false;
                    }
                    else {
                        digits.add(currentChar);
                    }
                }
            }
        }
        return true;
        
    }
}
