from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        head = 1
        tail = len(numbers)

        while head < tail:
            # number の中身は必ず昇順
            # 先端の値 (最小値) と最後尾の値 (最大値) を足していく
            # 2 つの合計値が小さすぎれば最小値を大きくして再計算
            # 2 つの合計値が大きすぎれば最大値を小さくして再計算
            total = numbers[head - 1] + numbers[tail - 1]

            if total < target:
                head += 1
            elif total > target:
                tail -= 1
            else:
                return [head, tail]


s = Solution()

# result = s.twoSum([2, 7, 11, 15], 9)
result = s.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8)

print(result)
