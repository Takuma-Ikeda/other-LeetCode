class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        while True:
            isOdd = False
            if n <= 1:
                break

            if n % 2 == 1:
                isOdd = True
                n -= 1

            n = n / 2
            matches += n
            n += 1 if isOdd else 0

        return int(matches)

# 模範解答
# https://leetcode.com/problems/count-of-matches-in-tournament/discuss/1004413/O(1)-Solution-Python-Easy


'''
class Solution:
    def numberOfMatches(self, n: int) -> int:
        # 結果は必ず n - 1 になる
        return n - 1
'''

# https://leetcode.com/problems/count-of-matches-in-tournament/discuss/1047565/Python-3-simple-and-O(1)-time-complexity

'''
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0

        while n != 1:
            # 試合数は floor (小数点切り捨て)
            # ex) 10.123 → 10
            count = count + math.floor(n / 2)

            # チーム数は ceil (小数点切り上げ)
            # ex) 10.123 → 11
            n = math.ceil(n / 2)

        return count
'''
