from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        # a - z の Unicode のコードポイントを割り当てた辞書型を作成
        new_morse_codes = dict()
        code_point = 97
        for m in morse_codes:
            new_morse_codes[code_point] = m
            code_point += 1

        # 変換されたモールスコードは集合型で管理する: 値の重複がないため
        converted_words = set()
        for w in words:
            convert = ''
            for c in w:
                convert += new_morse_codes[ord(c)]
            converted_words.add(convert)

        return len(converted_words)

# 模範解答
# https://leetcode.com/problems/unique-morse-code-words/discuss/348948/Python-3-using-dict-and-set


'''
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....",".." \
            ,".---","-.-",".-..","--","-.","---",".--.","--.-" \
            ,".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # コードポイントじゃなくて、単純にアルファベット a - z を key にしたいときはこうする
        D = dict(zip(string.ascii_lowercase, code))

        s = set()
        for word in words:
            # 内包表記を使うとシンプル
            s.add("".join([D[letter] for letter in word]))
        return len(s)
'''
