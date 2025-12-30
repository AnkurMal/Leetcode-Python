from collections import Counter
from typing import List
import numpy as np


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        new_board = np.array(board)
        for i in new_board:
            dic = Counter(i)
            if any(dic[key] > 1 for key in dic if key != "."):
                return False

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                dic = Counter(new_board[i : i + 3, j : j + 3].ravel())
                if any(dic[key] > 1 for key in dic if key != "."):
                    return False

        new_board = new_board.T
        for i in new_board:
            dic = Counter(i)
            if any(dic[key] > 1 for key in dic if key != "."):
                return False

        return True
