from typing import List


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row, data in enumerate(self.rectangle):
            for col, _ in enumerate(data):
                if (row1 <= row and row <= row2) and (col1 <= col and col <= col2):
                    self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

# 模範解答
# https://leetcode.com/problems/subrectangle-queries/discuss/685561/Python-Easier-solution


'''
class SubrectangleQueries(object):
    # copy:      新たな複合オブジェクトを作成し、その後、可能な限り、元のオブジェクト中に見つかったオブジェクトに対する「参照」を挿入
    # deep copy: 新たな複合オブジェクトを作成し、その後、元のオブジェクト中に見つかった「オブジェクトのコピー」を挿入
    def __init__(self, rectangle):
        self.rectangle = copy.deepcopy(rectangle)

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row, col):
        return self.rectangle[row][col]
'''

# https://leetcode.com/problems/subrectangle-queries/discuss/823195/Python-%2B-explanation

'''
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec = {}

        for i, row in enumerate(rectangle):
            self.rec[i] = row

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            self.rec[i] = self.rec[i][:col1] + [newValue] * (col2 - col1 + 1) + self.rec[i][col2 + 1:]

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]
'''
