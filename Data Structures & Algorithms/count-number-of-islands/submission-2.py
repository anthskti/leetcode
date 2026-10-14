class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # output: finding how many islands there are
        # since we're given a grid, we could use either bfs or dfs to outline the whole island. 
        # for each element, we can run dfs, if it exist and not seen yet, we can increase the count and re run dfs. 
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        count = 0

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r, c):
            if (r,c) in visited:
                return

            visited.add((r,c))
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not(0<=nr<ROWS) or not(0<=nc<COLS) or grid[nr][nc] != "1":
                    continue
                
                dfs(nr, nc)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    count += 1
        
        return count

        