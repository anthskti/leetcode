class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # returning the minimum minutes from 0 - minutes for all fruit to rot
        # from the diagram, we can see a heavy breadth first search graph forming
        # we create a queue of all the inital rotten fruit, let bfs onces each. 
        # we should snapshot this via a for loop so we can track time
        # we also need to track total fresh fruit, this is a way we can track all fruit can be rotten. 

        # time complexity should be O(m * n) where m is rows and n is columns 
        # space complexity O(n) from the queue.

        ROWS = len(grid) 
        COLS = len(grid[0])

        fresh = 0
        time = 0

        queue = []

        # checking every 2 - start point
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])

        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]

        while queue and fresh > 0:

            for i in range(len(queue)): # Snapshotting
                r, c = queue.pop(0)
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # if the row is out of count
                    if (not (0 <= nr < ROWS) 
                        or not (0 <= nc < COLS) 
                        or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    queue.append([nr,nc])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
        
    
        