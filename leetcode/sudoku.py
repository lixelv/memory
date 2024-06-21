from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_90 = [[board[j][i] for j in range(9)] for i in range(9)]

        for b in (board_90, board):
            for i in b:
                for j in i:
                    if j != "." and i.count(j) > 1:
                        return False

        for i in range(3):
            for j in range(3):
                box = [
                    board[i * 3 + i1][j * 3 + j1] for i1 in range(2) for j1 in range(3)
                ]
                for k in box:
                    if k != "." and box.count(k) > 1:
                        return False

        return True


print(
    Solution().isValidSudoku(
        [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ]
    )
)
