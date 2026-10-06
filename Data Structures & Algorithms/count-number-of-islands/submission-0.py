class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid),len(grid[0])
        visited = set()
        islands = 0

        def dfs(row_idx, col_idx):
            queue = deque([(row_idx, col_idx)])
            visited.add((row_idx, col_idx))

            while queue:
                row_idx, col_idx = queue.popleft()
                # directions that are one step away
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for direction in directions:
                    new_coord = (row_idx + direction[0], col_idx + direction[1])
                    # a valid next candidate is:
                    # - in bounds (row and col)
                    # - not visited yet
                    # - is a one
                    if ((0 <= new_coord[0] <= rows - 1) and
                    (0 <= new_coord[1] <= cols - 1) and
                    new_coord not in visited and
                    grid[new_coord[0]][new_coord[1]] == "1"):
                        queue.append(new_coord)
                        visited.add(new_coord)
                

        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == "1" and (row_idx, col_idx) not in visited:
                    dfs(row_idx, col_idx)
                    islands += 1
        
        return islands
