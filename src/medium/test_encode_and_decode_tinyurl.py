import unittest
from answer.encode_and_decode_tinyurl import Codec


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.longUrl = [
            'https://leetcode.com/problems/design-tinyurl'
        ]

    def test_solution(self):
        for i in range(len(self.longUrl)):
            print('----- TEST NO.%i START -----' % i)
            c = Codec()
            shortUrl = c.encode(self.longUrl[i])
            longUrl = c.decode(shortUrl)
            self.assertEqual(self.longUrl[i], longUrl)


if __name__ == "__main__":
    unittest.main()
