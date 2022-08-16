from collections import defaultdict


class Solution:
    def __init__(self):
        self.board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        self.mapAlphaPos = defaultdict(tuple)
        for i in range(len(self.board) - 1):
            for j in range(len(self.board[0])):
                self.mapAlphaPos[self.board[i][j]] = (i, j)
        self.mapAlphaPos['z'] = (5, 0)

    def alphabetBoardPath(self, target: str) -> str:
        
        def gotoAlphaFromXY(character, x, y):
            res = ''
            
            destX, destY = self.mapAlphaPos[character]
            if x==5 and y==0:
                while destX > x:
                    res += "D"
                    x += 1
                while destX < x:
                    res += "U"
                    x -= 1
                while destY > y:
                    res += "R"
                    y += 1
                while destY < y:
                    res += "L"
                    y -= 1
                return res+"!"
            while destY > y:
                res += "R"
                y += 1
            while destY < y:
                res += "L"
                y -= 1
            while destX > x:
                res += "D"
                x += 1
            while destX < x:
                res += "U"
                x -= 1
            return res+"!"

        res = ''
        x = 0
        y = 0
        for character in target:
            res += gotoAlphaFromXY(character, x, y)
            x, y = self.mapAlphaPos[character]
        return res
