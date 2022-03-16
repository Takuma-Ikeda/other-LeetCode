import unittest
from answer.merge_nodes_in_between_zeros import Solution, ListNode

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.head = [
            ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0)))))))),
            ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0)))))))),
        ]

        self.answers = [
            ListNode(4, ListNode(11)),
            ListNode(1, ListNode(3, ListNode(4))),
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            node = s.mergeNodes(self.head[i])

            while node:
                self.assertEqual(node.val, self.answers[i].val)
                node = node.next
                self.answers[i] = self.answers[i].next


if __name__ == "__main__":
    unittest.main()
