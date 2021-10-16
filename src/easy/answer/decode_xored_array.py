from typing import List


class Solution:
    # XOR について
    # https://wa3.i-3-i.info/word11658.html

    """
    例題1
    decoded [1,0,2,1]
    1 XOR 0 → 二進数計算「01 XOR 00 = 01」 → 十進数で 1 のこと
    0 XOR 2 → 二進数計算「00 XOR 10 = 10」 → 十進数で 2 のこと
    2 XOR 1 → 二進数計算「10 XOR 01 = 11」 → 十進数で 3 のこと
    → encorded [1, 2, 3]

    encoded [1, 2, 3] first 1
        → first は result[0]
    1 XOR 1 (result[0] XOR encoded[0])
        → 二進数計算「01 XOR 01 = 00」 → 十進数で 0 のこと: result[1]
    0 XOR 2 (result[1] XOR encoded[1])
        → 二進数計算「00 XOR 10 = 10」 → 十進数で 2 のこと: result[2]
    2 XOR 3 (result[2] XOR encoded[2])
        → 二進数計算「10 XOR 11 = 01」 → 十進数で 1 のこと: result[3]
    → decorded [1, 0, 2, 1]
    """

    """
    例題2
    decoded [4, 2, 0, 7, 4]
    4 XOR 2 → 二進数計算「100 XOR 010 = 110」 → 十進数で 6 のこと
    2 XOR 0 → 二進数計算「010 XOR 000 = 010」 → 十進数で 2 のこと
    0 XOR 7 → 二進数計算「000 XOR 111 = 111」 → 十進数で 7 のこと
    7 XOR 4 → 二進数計算「111 XOR 100 = 011」 → 十進数で 3 のこと
    → encorded [6, 2, 7, 3]

    encoded [6, 2, 7, 3] first 4
        → first は result[0]
    4 XOR 6 (result[0] XOR encoded[0])
        → 二進数計算「100 XOR 110 = 010」 → 十進数で 2 のこと: result[1]
    2 XOR 2 (result[1] XOR encoded[1])
        → 二進数計算「010 XOR 010 = 000」 → 十進数で 0 のこと: result[2]
    0 XOR 7 (result[2] XOR encoded[2])
        → 二進数計算「000 XOR 111 = 111」 → 十進数で 7 のこと: result[3]
        7 XOR 3 (result[3] XOR encoded[3])
        → 二進数計算「111 XOR 011 = 100」 → 十進数で 4 のこと: result[4]
    → decorded [4, 2, 0, 7, 4]
    """

    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in encoded:
            # ^ は XOR 演算子
            result.append(result[-1] ^ i)
        return result
