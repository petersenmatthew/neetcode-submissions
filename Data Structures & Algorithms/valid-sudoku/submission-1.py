class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # cols = array of 9 sets 
       # rows = array of 9 sets
       cols = [set() for _ in range(9)]
       rows = [set() for _ in range(9)] 
       sub_boxes = [[set() for _ in range(3)] for _ in range(3)]


       for row_index, row in enumerate(board):
            for col_index, cur_num in enumerate(row):

                # empty tile
                if cur_num == ".":
                    continue
                # check if in that column theres a duplicate
                if cur_num in cols[col_index]:
                    return False
                else:
                    cols[col_index].add(cur_num)

                # check if in that row theres a duplicate
                if cur_num in rows[row_index]:
                    return False
                else:
                    rows[row_index].add(cur_num)

                # check the sub box:
                box_row = row_index // 3
                box_col = col_index // 3
                if cur_num in sub_boxes[box_row][box_col]:
                    return False
                else:
                    sub_boxes[box_row][box_col].add(cur_num)
       return True