class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 9 sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                # compute index of the 3x3 sub‑box
                box_index = (i // 3) * 3 + (j // 3)
                # check for duplicates
                if (val in rows[i]) or (val in cols[j]) or (val in boxes[box_index]):
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
        return True
