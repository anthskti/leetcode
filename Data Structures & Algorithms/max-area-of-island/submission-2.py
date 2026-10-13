class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # we have to output the biggest island number
        # this does look like bfs approach where we can count down to the deepest until we run out, and track how far it goes.
        # we can compare the islands maxes and return that
        # DFS approach.
        # O(rows x cols) time complexity

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        max_area = 0

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(row, col, area):
            if (row, col) in visited:
                return 0
            
            visited.add((row,col))

            area = 1
            
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (not(0 <= nr < ROWS) 
                    or not(0 <= nc < COLS) 
                    or grid[nr][nc] != 1):
                    continue
                
                area += dfs(nr,nc,area)
            return area




        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col, 0)
                    max_area = max(max_area, area)

        return max_area
        