from typing import List

class OrderedStream:

    # Python のメンバ変数は不要
    n = 0
    values = {}
    isInserted = {}
    isReturned = {}

    def __init__(self, n: int):
        self.n = n
        for i in range(n):
            i += 1
            self.values[i] = 0
            self.isInserted[i] = False
            self.isReturned[i] = False

    def insert(self, idKey: int, value: str) -> List[str]:
        result = []
        self.isInserted[idKey] = True
        self.values[idKey] = value

        for i in range(self.n):
            i += 1
            if self.isInserted[i] == False:
                break
            else:
                if not self.isReturned[i] == True:
                    result += [self.values[i]]
                self.isReturned[i] = True

        return result

# 模範解答
# https://leetcode.com/problems/design-an-ordered-stream/discuss/954502/Python-solution-easy-and-straight-forward


'''
class OrderedStream:
    def __init__(self, n: int):
        # None が入った List を作成
        self.stream = [None] * (n + 1)
        self.temp = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        ans = []
        while self.temp < len(self.stream) and self.stream[self.temp]:
            ans.append(self.stream[self.temp])
            self.temp += 1
        return ans
'''
