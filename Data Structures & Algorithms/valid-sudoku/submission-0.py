class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input 9x9 array in an array
        # could be empty squares ="."
        # output true or false if sudoku

        # brute: O(n^2)
        # for [i][j], check all of [i][j+] and [i+][j] see if they contain itself
        # how do i account for the square though
        # row (i / 3) 
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        n = len(board)
        
        # Check duplicates 
        for r in range(9):
            for c in range (9):
                if board[r][c] == ".": 
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True
        