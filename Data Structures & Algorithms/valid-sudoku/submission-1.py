class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input 9x9 array in an array
        # could be empty squares ="."
        # output true or false if sudoku

        # brute: O(n^2)
        # for [i][j], check all of [i][j+] and [i+][j] see if they contain itself
        # how do i account for the square though
        # row (i / 3) 
        
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        n = len(board)
        
        # Check duplicates 
        for r in range(9):
            for c in range (9):
                if board[r][c] == ".": 
                    continue


                val = board[r][c] 
                idx = (r//3)*3 + (c//3) 
                if (val in rows[r] or 
                    val in cols[c] or
                    val in squares[idx]):
                    return False

                cols[c].add(val)
                rows[r].add(val)
                squares[idx].add(val)

        return True
        