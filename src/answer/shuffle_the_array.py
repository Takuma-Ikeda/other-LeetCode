from typing import List


class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        l1 = nums[0:n]  # nums[:n] でもよい
        l2 = nums[n:]

        for i in range(len(l1)):
            result.append(l1[i])
            result.append(l2[i])
            # result += [l1[i], l2[i]] でもよい

        return result


# 模範解答
# https://leetcode.com/problems/shuffle-the-array/discuss/675110/Easiest-python-solution-with-zip-O(n)-time

'''
def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]
        return res
'''

# zip関数について

'''
names = ['taro', 'hanako', ‘'jiro']
ages = [25, 30, 27]

# 複数のリストを同時に for 文で回すことができる
for name, age in zip(names, ages):
    print(name, age)

# taro 25
# hanako 30
# jiro 27
'''
