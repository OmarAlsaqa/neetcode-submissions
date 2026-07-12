class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            hr = dict()
            hc = dict()
            hb = dict()
            for j, col in enumerate(row):
                hr[col] = hr.get(col, 0) + 1
                # print(col)
                if (hr[col] > 1) and (col != "."):
                    # print('hr', hr)
                    return False
                
                hc[board[j][i]] = hc.get(board[j][i], 0) + 1
                if hc[board[j][i]] > 1 and board[j][i] != ".":
                    # print('hc', hc)
                    return False
                
                bb = board[(i%3)*3 + j//3][(i//3)*3 + j%3]
                hb[bb] = hb.get(bb, 0) + 1
                # print(bb)
                if hb[bb] > 1 and bb != ".":
                    # print('hb', hb)
                    return False
        return True

                