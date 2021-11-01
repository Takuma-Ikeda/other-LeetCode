import unittest
from answer.subrectangle_queries import SubrectangleQueries


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.methods = [
            ["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue", "updateSubrectangle", "getValue", "getValue"],
            ["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue", "updateSubrectangle", "getValue"],
        ]
        self.args = [
            [
                [
                    [
                        [1, 2, 1],
                        [4, 3, 4],
                        [3, 2, 1],
                        [1, 1, 1],
                    ],
                ],
                [0, 2],
                [0, 0, 3, 2, 5],
                [0, 2],
                [3, 1],
                [3, 0, 3, 2, 10],
                [3, 1],
                [0, 2],
            ],
            [
                [
                    [
                        [1, 1, 1],
                        [2, 2, 2],
                        [3, 3, 3],
                    ],
                ],
                [0, 0],
                [0, 0, 2, 2, 100],
                [0, 0],
                [2, 2],
                [1, 1, 2, 2, 20],
                [2, 2],
            ],
        ]
        self.answers = [
            [None, 1, None, 5, 5, None, 10, 5],
            [None, 1, None, 100, 100, None, 20],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            result = []
            print('----- TEST NO.%i START -----' % i)

            for j in range(len(self.methods[i])):
                if self.methods[i][j] == 'SubrectangleQueries':
                    s = SubrectangleQueries(self.args[i][j][0])
                    result.append(None)
                elif self.methods[i][j] == 'getValue':
                    result.append(
                        s.getValue(
                            self.args[i][j][0],
                            self.args[i][j][1]
                        ))
                elif self.methods[i][j] == 'updateSubrectangle':
                    result.append(
                        s.updateSubrectangle(
                            self.args[i][j][0],
                            self.args[i][j][1],
                            self.args[i][j][2],
                            self.args[i][j][3],
                            self.args[i][j][4]
                        ))

            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
