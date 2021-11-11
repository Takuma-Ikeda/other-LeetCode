import unittest
from answer.group_the_people_given_the_group_size_they_belong_to import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.groupSizes = [
            [3, 3, 3, 3, 3, 1, 3],
            [2, 1, 3, 3, 3, 2],
        ]

        self.answers = [
            [[5], [0, 1, 2], [3, 4, 6]],
            [[1], [0, 5], [2, 3, 4]],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.groupThePeople(self.groupSizes[i])

            for r in result:
                for idx, a in enumerate(self.answers[i]):
                    if set(a) == set(r):
                        self.answers[i].pop(idx)
                        break

            # すべて pop できたなら [] になる
            self.assertTrue(self.answers[i] == [])


if __name__ == "__main__":
    unittest.main()
