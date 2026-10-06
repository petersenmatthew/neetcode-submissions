class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row_idx, col_idx):
            queue = deque([(row_idx, col_idx)])
            visited.add((row_idx, col_idx))
            cur_size = 1

            while queue:
                row_idx, col_idx = queue.popleft()
                directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

                for direction in directions:
                    new_coord = (row_idx + direction[0], col_idx + direction[1])
                    # this new coord has to be:
                    # - in bounds of rows
                    # - in bounds of cols
                    # a "1"
                    # not visited
                    if (0 <= new_coord[0] < rows and
                    0 <= new_coord[1] < cols and
                    grid[new_coord[0]][new_coord[1]] == 1 and
                    new_coord not in visited):
                         cur_size += 1
                         queue.append(new_coord)
                         visited.add(new_coord)
            return cur_size


        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == 1 and (row_idx, col_idx) not in visited:
                    island_size = dfs(row_idx, col_idx)
                    maxIsland = max(island_size, maxIsland)
        return maxIsland