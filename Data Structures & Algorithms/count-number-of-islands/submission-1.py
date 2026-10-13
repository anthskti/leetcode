class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # our output should return the total number of islands in the grid
        # since we're looking at connectivity, we could utilize DFS or BFS 
        # for DFS, we're covering all 1's land, then put it in a set. 
        # for each element, we can check if its visited, and run dfs

        # time complexity O(rows * cols)

        ROWS = len(grid)
        COLS = len(grid[0])

        islands = 0

        visited = set()

        directions = [
            [0,1], 
            [0,-1], 
            [1,0], 
            [-1,0]
        ]
        def dfs(row, col):
            # if its visited, no need to rerun
            if (row, col) in visited:
                return 
            
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (not (0 <= nr < ROWS) 
                or not (0 <= nc < COLS) 
                or grid[nr][nc] != "1"):
                    continue
                
                dfs(nr, nc)

                

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row, col)
                    islands+=1

        return islands
                

        