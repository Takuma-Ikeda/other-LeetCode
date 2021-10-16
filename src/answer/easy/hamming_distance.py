class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 1 になっているビットの数を数えること: popcount (population count)
        # XOR で計算して、二進数表記して popcount すること: ハミング距離
        return bin(x ^ y).count('1')
