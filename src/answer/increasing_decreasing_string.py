class Solution:
    def sortString(self, s: str) -> str:
        result = ''
        d = dict()

        # key: Unicode コードポイント
        # value: 出現回数
        for v in s:
            v = ord(v)
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

        # 辞書型に要素が存在する限りループする
        while any(d):
            # step 1 - 3
            for v in range(97, 123):
                if v in d:
                    d[v] -= 1
                    result += chr(v)

                    if d[v] == 0:
                        del d[v]

            # step 4 - 6
            for v in range(123, 96, -1):
                if v in d:
                    d[v] -= 1
                    result += chr(v)

                    if d[v] == 0:
                        del d[v]

        return result

# 模範解答
# https://leetcode.com/problems/increasing-decreasing-string/discuss/543172/Python-3-Using-Set-and-Sort-with-commentary


'''
class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)

        # 結果は配列要素として持っておいて、最後にまとめて join したほうがいい
        result = []

        while len(s) > 0:
            # 集合型を作成して昇順ソート
            smallest = sorted(set(s))

            for small in smallest:
                result.append(small)
                s.remove(small)

            # 集合型を作成して降順ソート
            largest = sorted(set(s), reverse = True)

            for large in largest:
                result.append(large)
                s.remove(large)

        return ''.join(result)
'''
