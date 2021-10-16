from typing import List


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big = self.big - 1
            return True if (self.big >= 0) else False
        if carType == 2:
            self.medium = self.medium - 1
            return True if (self.medium >= 0) else False
        if carType == 3:
            self.small = self.small - 1
            return True if (self.small >= 0) else False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# 模範解答
# https://leetcode.com/problems/design-parking-system/discuss/955808/Simple-and-fast-solution-(96.55)


'''
class ParkingSystem:
    # 辞書型オブジェクトの作成
    places = dict()
    
    def __init__(self, big: int, medium: int, small: int):
        # 辞書型オブジェクトに数値を保存
        self.places[1] = big
        self.places[2] = medium
        self.places[3] = small
        
    def addCar(self, carType: int) -> bool:
        if self.places[carType] > 0:
            self.places[carType] -= 1
            return True
        else:
            return False
'''
