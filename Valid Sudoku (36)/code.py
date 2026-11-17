class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        horizontal_seen = set()
        vertical_seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in horizontal_seen:
                        return False
                    horizontal_seen.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in vertical_seen:
                        return False
                    vertical_seen.add(board[j][i])
            horizontal_seen = set()
            vertical_seen = set()

        sub_box_seen = set()
        a = 0
        b = 0
        c = 0
        t = True
        while c < 9:
            if board[a][b] != ".":
                if board[a][b] in sub_box_seen:
                    return False
                sub_box_seen.add(board[a][b])
            if a % 3 < 2 and b % 3 == 2:
                a += 1
                b -= 2
            elif a % 3 == 2 and b % 3 == 2:
                sub_box_seen = set()
                if c % 3 == 2:
                    t = False
                if t:
                    c += 1
                    a -= 2
                    b += 1
                else:
                    c += 1
                    a += 1
                    b = 0
                    t = True
            else:
                b += 1
        return True
