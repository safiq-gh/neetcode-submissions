class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for x in range(len(board))]
        cols = [[] for x in range(len(board[0]))]
        boxes = [[] for x in range(len(board))]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                box = (r // 3) * 3 + (c // 3)

                if num == ".":
                    continue
                elif num in rows[r] or num in cols[c] or num in boxes[box]:
                    return False
                else:
                    rows[r].append(num)
                    cols[c].append(num)
                    boxes[box].append(num)
        return True        

