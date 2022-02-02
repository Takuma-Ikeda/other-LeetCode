import unittest
from answer.maximum_twin_sum_of_a_linked_list import Solution, ListNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.head = [
            ListNode(5, ListNode(4, ListNode(2, ListNode(1)))),
            ListNode(4, ListNode(2, ListNode(2, ListNode(3)))),
        ]
        self.answers = [
            6,
            7,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.pairSum(self.head[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
