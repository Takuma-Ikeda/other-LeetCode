import unittest
from answer.defanging_an_ip_address import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.addresses = [
            "1.1.1.1",
            "255.100.50.0"
        ]
        self.answers = [
            "1[.]1[.]1[.]1",
            "255[.]100[.]50[.]0"
        ]

    def solution(self, i):
        s = Solution()
        result = s.defangIPaddr(self.addresses[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
