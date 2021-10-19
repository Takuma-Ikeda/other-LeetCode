import unittest
from answer.number_of_recent_calls import RecentCounter


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input1 = [
            [[], [1], [100], [3001], [3002]]
        ]
        self.input2 = [
            ["RecentCounter", "ping", "ping", "ping", "ping"],
        ]
        self.answers = [
            [None, 1, 2, 3, 3],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)

            for i1, i2, answer in zip(self.input1[i], self.input2[i], self.answers[i]):

                if i2 == "RecentCounter":
                    r = RecentCounter()
                elif i2 == "ping":
                    self.assertEqual(answer, r.ping(i1[0]))


if __name__ == "__main__":
    unittest.main()
