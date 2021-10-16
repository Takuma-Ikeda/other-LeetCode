import unittest
from answer.easy.convert_binary_number_in_a_linked_list_to_integer import Solution, ListNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.head = [
            ListNode(1, ListNode(0, ListNode(1, None))),
            ListNode(0, None),
            ListNode(1, None),
            ListNode(1,
                ListNode(0,
                    ListNode(0,
                        ListNode(1,
                            ListNode(0,
                                ListNode(0,
                                    ListNode(1,
                                        ListNode(1,
                                            ListNode(1,
                                                ListNode(0,
                                                    ListNode(0,
                                                        ListNode(0,
                                                            ListNode(0,
                                                                ListNode(0,
                                                                    ListNode(0, None)
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            ListNode(0, ListNode(0, None)),
        ]

        self.answers = [
            5,
            0,
            1,
            18880,
            0,
        ]

    def solution(self, i):
        s = Solution()
        result = s.getDecimalValue(self.head[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)

    def test_solution3(self):
        self.solution(3)

    def test_solution4(self):
        self.solution(4)


if __name__ == "__main__":
    unittest.main()
