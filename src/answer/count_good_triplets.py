from typing import List

# 模範解答
# https://leetcode.com/problems/count-good-triplets/discuss/772455/Python-sol-with-generator-and-loops


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        size = len(arr)
        good_count = 0

        # 組み合わせを作成: i, j, k それぞれが現在使っている index が互いに重複しないような range 設定にする
        for i in range(0, size - 2):
            for j in range(i + 1, size - 1):
                for k in range(j + 1, size):

                    # abs は絶対値を取得
                    ok_a = abs(arr[i] - arr[j]) <= a
                    ok_b = abs(arr[j] - arr[k]) <= b
                    ok_c = abs(arr[i] - arr[k]) <= c

                    # all: すべてが True なら True
                    if all((ok_a, ok_b, ok_c)):
                        good_count += 1

        return good_count


'''
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def is_good(i, j, k):
            ok_a = abs(arr[i] - arr[j]) <= a
            ok_b = abs(arr[j] - arr[k]) <= b
            ok_c = abs(arr[i] - arr[k]) <= c
            return all((ok_a, ok_b, ok_c))

        size = len(arr)
        # True だったら 1 を sum する
        return sum(1 for i in range(0, size - 2) for j in range(i + 1, size - 1) for k in range(j + 1, size) if is_good(i, j, k))
'''
