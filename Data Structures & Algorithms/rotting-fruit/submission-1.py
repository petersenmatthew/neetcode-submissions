class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0

        rows, cols = len(grid), len(grid[0])
        fresh_fruit = set()
        queue = deque()
        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == 2:
                    queue.append((row_idx, col_idx))
                elif grid[row_idx][col_idx] == 1:
                    fresh_fruit.add((row_idx, col_idx))
        while queue:
            level_size = len(queue)
            found = False
            for _ in range(level_size):
                row_idx, col_idx = queue.popleft()
                directions = [(1,0), (-1,0), (0, 1), (0, -1)]
                for direction in directions:
                    new_coord = (row_idx + direction[0], col_idx + direction[1])
                    if (0 <= new_coord [0] < rows and
                    0 <= new_coord[1] < cols and
                    grid[new_coord[0]][new_coord[1]] == 1):
                        grid[new_coord[0]][new_coord[1]] = 2
                        queue.append(new_coord)
                        fresh_fruit.remove((new_coord[0], new_coord[1]))
                        found = True
            
            if found:
                minutes +=1
        if fresh_fruit:
            return -1
        return minutes