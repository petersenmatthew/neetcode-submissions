class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        def bfs ():
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                row_idx, col_idx = queue.popleft()
                for direction in directions:
                    # check that its infinity (not visited candidate) and bounded
                    new_coord = (row_idx + direction[0], col_idx + direction[1])
                    if (0 <= new_coord[0] < rows and
                    0 <= new_coord[1] < cols and
                    grid[new_coord[0]][new_coord[1]] == 2147483647):
                        queue.append(new_coord)
                        grid[new_coord[0]][new_coord[1]] = grid[row_idx][col_idx] + 1




        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == 0:
                    queue.append((row_idx, col_idx))

        bfs()
                    