class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int row=0; row<9; row++) //iterating through the rows
        {
            unordered_set <char> seen; //Create a set to look for unique values
            for (int i=0; i<9; i++)
            {
                if(board[row][i]=='.') continue; //Continues if it is empty
                if(seen.count(board[row][i])) return false; //Returns if seen in the set before
                seen.insert(board[row][i]); //Adds to the set
            }
        }
        for (int column =0; column<9; column++) //Same thing as before but iterating through the columns
        {
            unordered_set <char> seen;
            for (int i=0; i<9; i++)
            {
                if(board[i][column]=='.') continue;
                if(seen.count(board[i][column])) return false;
                seen.insert(board[i][column]);
            }
        }
        for (int square=0; square<9; square++)
        {
            unordered_set <char> seen;
            for (int i= 0; i < 3; i++)
            {
                for (int j=0; j<3; j++)
                {

                
                int row=(square/3) * 3 + i;
                int column=(square %3) * 3 + j; 
                if(board[row][column]=='.') continue;
                if(seen.count(board[row][column])) return false;
                seen.insert(board[row][column]);
            }
        }
        }
        return true;
    }
};
