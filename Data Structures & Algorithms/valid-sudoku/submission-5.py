class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            rows = [[] for _ in range(len(board))]
            cols = [[] for _ in range(len(board))]
            boxes = [[] for _ in range(9)]

            for r in range(len(rows)):
                for c in range(len(cols)):
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



