class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int j=0; j<9; j++) //iterating through the rows
        {
            unordered_set <char> seen; //Create a set to look for unique values
            for (int i=0; i<9; i++)
            {
                if(board[j][i]=='.') continue; //Continues if it is empty
                if(seen.count(board[j][i])) return false; //Returns if seen in the set before
                seen.insert(board[j][i]); //Adds to the set
            }
        }
        for (int j =0; j<9; j++) //Same thing as before but iterating through the columns
        {
            unordered_set <char> seen;
            for (int i=0; i<9; i++)
            {
                if(board[i][j]=='.') continue;
                if(seen.count(board[i][j])) return false;
                seen.insert(board[i][j]);
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
