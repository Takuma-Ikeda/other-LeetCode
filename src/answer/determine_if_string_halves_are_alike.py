class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count_a = count_b = 0
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        half = int(len(s) / 2)
        a = s[:half]
        b = s[half:]

        for c_a, c_b in zip(a, b):
            if c_a in vowels:
                count_a += 1

            if c_b in vowels:
                count_b += 1

        return count_a == count_b

# 模範解答
# https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/988173/Python-easy-Solution-O(N)-ACCEPTED


'''
class Solution:
    def halvesAreAlike(s):
        vowels_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        count = 0
        i, j = 0, len(s)//2
        while j < len(s):
            if s[i] in vowels_set:
                count += 1

            if s[j] in vowels_set:
                count -= 1

            i += 1
            j += 1

        return count == 0
'''
