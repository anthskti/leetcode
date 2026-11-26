class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]):
        # return the number of empty cells that no guard can see
        # guards can see row and column

        
        # brute force: for every [x, 0], [0, x] can see unless, break
        # 1 to guard
        # 2 to wall
        # 3 to what guard can see

        grid = [[0] * n for _ in range(m)]

        # initalize walls
        for x, y in walls:
            grid[x][y] = 1

        # initalize guards
        for x,y in guards:
            grid[x][y] = 2

        for x, y in guards:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a = x + dx
                b = y + dy
                while 0 <= a < m and 0 <= b < n and grid[a][b] not in (1, 2):
                    grid[a][b] = 3
                    a += dx
                    b += dy


        # count all empty
        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    count += 1
        return count


        
