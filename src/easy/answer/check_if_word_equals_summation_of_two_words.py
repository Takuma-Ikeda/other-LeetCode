class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        def convertInt(s) -> int:
            # 先頭 a をトリム
            while s.startswith('a'):
                s = s[1:]

            # 全部 a だった場合
            if not s:
                return 0

            result = []
            [result.append(str(ord(v) - 97)) for v in s]
            return int(''.join(result))

        return (convertInt(firstWord) + convertInt(secondWord)) == convertInt(targetWord)
