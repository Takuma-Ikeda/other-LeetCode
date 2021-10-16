import unittest
from answer.count_items_matching_a_rule import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.items = [
            [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
            [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
        ]
        self.ruleKey = [
            'color',
            'type'
        ]
        self.ruleValue = [
            'silver',
            'phone'
        ]
        self.answers = [
            1,
            2,
        ]

    def solution(self, i):
        s = Solution()
        result = s.countMatches(self.items[i], self.ruleKey[i], self.ruleValue[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
