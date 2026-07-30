# Intuition
# Brute force method: 
# Index word, check every value that is [i][j+1] or [i+1][j]
# j is our x axis, i is our y axis


# my logic: find all the positions of word[0] --> run [i][j+1] or [i+1][j] algo on it. return true if res == len(word)

# re. my logic: have a new grid, add [i][j-1] or [i-1][j] 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, i):
            # Means it exists
            if i == len(word):
                return True
            if r < 0 or c < 0 or r>=rows or c>=cols or word[i] != board[r][c] or visited[r][c]:
                return False
            
            visited[r][c] = True
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            visited[r][c] = False
            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


    def dp_exist(self, board: List[List[str]], word: str) -> List[List[str]]:
        grid = [[0 for col in range(len(board[0]))] for row in range(len(board))]

        count = 0

        # Base Case
        if board[0][0] == word[0]:
            grid[0][0] = 1

        for i in range(1, len(board)): # Cols
            if board[i][0] == word[grid[i-1][0]]:
                grid[i][0] += grid[i-1][0] + 1
        for j in range(1, len(board[0])): # Rows
            if board[0][j] == word[grid[0][j-1]]:
                grid[0][j] += grid[0][j-1] + 1

        
        # Checking each character to see if it matches the word
        for i in range(1, len(board)): # column
            for j in range(1, len(board[0])): # row
                m = max(grid[i][j-1], grid[i-1][j])
                if m == len(word):
                    return True
                if board[i][j] == word[m]:
                    grid[i][j] = m+1
                

        return False