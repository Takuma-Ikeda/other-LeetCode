import unittest
from answer.easy.design_parking_system import ParkingSystem


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            [
                ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"],
                [[1, 1, 0], [1], [2], [3], [1]]
            ]
        ]
        self.answers = [
            [None, True, True, False, False],
        ]

    def solution(self, i):
        result = []
        for keys, values in zip(self.input[i][0], self.input[i][1]):
            if keys == "ParkingSystem":
                p = ParkingSystem(values[0], values[1], values[2])
                result += [None]
            else:
                result += [p.addCar(values[0])]
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)


if __name__ == "__main__":
    unittest.main()
