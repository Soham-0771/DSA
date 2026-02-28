class Solution:
    def solveSudoku(self, board) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        # Initialize bitmasks
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    num = int(board[r][c])
                    mask = 1 << num
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + c // 3] |= mask

        def backtrack(idx):
            if idx == len(empties):
                return True

            r, c = empties[idx]
            box = (r // 3) * 3 + c // 3
            used = rows[r] | cols[c] | boxes[box]

            for num in range(1, 10):
                mask = 1 << num
                if not (used & mask):
                    board[r][c] = str(num)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box] |= mask

                    if backtrack(idx + 1):
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r] ^= mask
                    cols[c] ^= mask
                    boxes[box] ^= mask

            return False

        backtrack(0)
