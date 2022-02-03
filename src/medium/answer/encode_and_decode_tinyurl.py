from random import randint


# 模範解答
# https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/448840/Python-3-(beats-98)-(Dictionary)
class Codec:
    def __init__(self):
        self.tiny_urls = {}

    def encode(self, longUrl: str) -> str:
        num_form = randint(1, 1E10)

        while num_form in self.tiny_urls:
            # 1E10 は 10^10 の意味。つまり 100 億
            num_form = randint(1, 1E10)

        self.tiny_urls[num_form] = longUrl

        return 'https://leetcode.com/' + str(num_form)

    def decode(self, shortUrl: str) -> str:
        return self.tiny_urls[int(shortUrl[21:])]
