class RecentCounter:

    def __init__(self):
        self.t = []

    def ping(self, t: int) -> int:
        self.t.append(t)
        last_idx = len(self.t) - 1

        # 初回
        if last_idx == 0:
            return len(self.t)

        is_outdated = False
        outdated_idx = 0

        for idx, _ in enumerate(self.t):
            if (self.t[last_idx] - self.t[idx]) >= 3001:
                is_outdated = True
                outdated_idx = idx
            else:
                # 途中から 3000 以下の要素ばかりになるのでループ中断: しないと処理が重くなる
                break

        if is_outdated:
            self.t = self.t[outdated_idx + 1:]

        return len(self.t)


# 模範解答
# https://leetcode.com/problems/number-of-recent-calls/discuss/873418/Python-and-C%2B%2B-Multiple-approaches-Binary-search-Dequeue


'''
# USING DEQUE
# Python のコンテナデータ型の１種。
# データの追加を先頭・末尾の両方・または好きな方に O(1) のコストで行う
# append():     末尾にデータを追加
# appendleft(): 先頭にデータを追加
# pop():        dequeの右側の要素を削除して返す
# popleft():    dequeの左側の要素を削除して返す

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        queue.append(t)

        # キューが存在するかつ、一番左側の要素が 3000 以内であること
        while queue and (queue[0] < t - 3000):
            # 一番左側の要素を削除
            queue.popleft()

        return len(queue)
'''

'''
# USING BINARY SEARCH
class RecentCounter:
    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        start = t - 3000

        if t <= 0:
            return len(self.arr)

        # 関数内関数
        def binSearch(start,arr):
            i = 0
            j = len(arr)

            while i <= j:
                mid = (i + j) // 2

                if arr[mid] > start:
                    j = mid - 1
                elif arr[mid] < start:
                    i = mid + 1
                else:
                    return mid

            return i

        indx = binSearch(start, self.arr)
        return len(self.arr) - indx
'''
