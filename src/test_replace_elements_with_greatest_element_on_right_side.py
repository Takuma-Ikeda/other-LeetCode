import unittest
from answer.easy.replace_elements_with_greatest_element_on_right_side import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr = [
            [17, 18, 5, 4, 6, 1],
            [400],
        ]
        self.answers = [
            [18, 6, 6, 6, 1, -1],
            [-1],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.replaceElements(self.arr[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
