class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # say matrix is m x n
        # for it to flow to pacific:
        # has to be able to reach the top left edges
        # either row = 0
        # or col = 0

        # for it to flow to atlantic:
        # has to be able to reach the bottom right edges
        # either row = len(rows) - 1
        # or col = len(cols) - 1

        rows, cols = len(heights),len(heights[0])
        pacific_queue = deque()
        atlantic_queue = deque()

        pacific_visited = set()
        atlantic_visited = set()

        output = []
        def bfs(queue, visited):
            while queue:
                row_idx, col_idx = queue.popleft()
                
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for direction in directions:
                    new_coord = (row_idx + direction[0], col_idx + direction[1])
                    # a valid next candidate is:
                    # - in bounds (row and col)
                    # - not visited yet
                    # - has a value lower
                    if (0 <= new_coord[0] < rows and
                    0 <= new_coord[1] < cols and
                    new_coord not in visited
                    and heights[new_coord[0]][new_coord[1]] >= heights[row_idx][col_idx]):
                        visited.add(new_coord)
                        queue.append(new_coord)

        for row_idx in range(rows):
            for col_idx in range(cols):
                if row_idx == 0 or col_idx == 0:
                    pacific_queue.append((row_idx, col_idx))
                    pacific_visited.add((row_idx, col_idx))

                if row_idx == rows - 1 or col_idx == cols - 1:
                    atlantic_queue.append((row_idx, col_idx))
                    atlantic_visited.add((row_idx, col_idx))

        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)
        for row_idx in range(rows):
            for col_idx in range(cols):
                if (row_idx, col_idx) in atlantic_visited and (row_idx, col_idx) in pacific_visited:
                    output.append([row_idx, col_idx])
        
        return output

            

        