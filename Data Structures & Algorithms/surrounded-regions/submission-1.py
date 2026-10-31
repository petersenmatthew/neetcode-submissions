class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = deque()
        
        # iterate through borders

        # top border
        for i in range(cols):
            queue.append((0, i))
        
        # bottom
        for i in range(cols):
            queue.append((rows - 1, i))

        # left
        for i in range(rows):
            queue.append((i, 0))
        # right
        for i in range(rows):
            queue.append((i, cols - 1))



        while queue:
            row_idx, col_idx = queue.popleft()
            if board[row_idx][col_idx] != "O":
                continue 
            else:
                board[row_idx][col_idx] = "S"
            
            directions = [(1,0), (-1,0), (0,1),(0,-1)]

            for direction in directions:
                new_coord = (row_idx + direction[0], col_idx + direction[1])
                # ensure in bound
                if (0 <= new_coord[0] < rows and
                0 <= new_coord[1] < cols and
                board[new_coord[0]][new_coord[1]] == "O"):
                    queue.append((new_coord[0],new_coord[1]))
            
        for row_idx in range(rows):
            for col_idx in range(cols):
                if board[row_idx][col_idx] == "O":
                    board[row_idx][col_idx] = "X"
                elif board[row_idx][col_idx] == "S":
                    board[row_idx][col_idx] = "O"
        
