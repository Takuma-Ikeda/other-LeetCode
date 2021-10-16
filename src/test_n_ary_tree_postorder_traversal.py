import unittest
from answer.easy.n_ary_tree_postorder_traversal import Solution, Node


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.root = [
            Node(1, [
                Node(3, [
                    Node(5),
                    Node(6),
                ]),
                Node(2),
                Node(4),
            ]),
            Node(1, [
                Node(2),
                Node(3, [
                    Node(6),
                    Node(7, [
                        Node(11, [
                            Node(14),
                        ])
                    ])
                ]),
                Node(4, [
                    Node(8, [
                        Node(12),
                    ])
                ]),
                Node(5, [
                    Node(9, [
                        Node(13),
                    ]),
                    Node(10),
                ])
            ]),
        ]
        self.answers = [
            [5, 6, 3, 2, 4, 1],
            [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
        ]

    def solution(self, i):
        s = Solution()
        result = s.postorder(self.root[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
