class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        
        def dfs(row_idx, col_idx):
            if board[row_idx][col_idx] != "O":
                return 
            else:
                board[row_idx][col_idx] = "S"
            
            directions = [(1,0), (-1,0), (0,1),(0,-1)]

            for direction in directions:
                new_coord = (row_idx + direction[0], col_idx + direction[1])
                # ensure in bound
                if (0 <= new_coord[0] < rows and
                0 <= new_coord[1] < cols and
                board[new_coord[0]][new_coord[1]] == "O"):
                    dfs(new_coord[0],new_coord[1])
            
        # iterate through borders

        # top border
        for i in range(cols):
            dfs(0, i)
        
        # bottom
        for i in range(cols):
            dfs(rows - 1, i)

        # left
        for i in range(rows):
            dfs(i, 0)
        # right
        for i in range(rows):
            dfs(i, cols - 1)


        for row_idx in range(rows):
            for col_idx in range(cols):
                if board[row_idx][col_idx] == "O":
                    board[row_idx][col_idx] = "X"
                elif board[row_idx][col_idx] == "S":
                    board[row_idx][col_idx] = "O"
        
