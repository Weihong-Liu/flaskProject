import random
import string


class ExchangeCode:
    def __init__(self, rand_len=13, prefix="TX"):
        self.rand_len = rand_len  # 这里可以随意传入想要生成的位数
        self.rand_limit = 36 ** rand_len
        self.prefix = prefix  # 前缀

    def _int_to_str(self, x, base=36):
        numerals = string.digits + string.ascii_lowercase + string.ascii_uppercase
        numerals.replace('0', '')
        numerals.replace('o', '')
        if x == 0:
            return numerals[0]
        sign = -1 if x < 0 else 1
        x *= sign
        digits = []
        while x:
            digits.append(numerals[x % base])
            x /= base
            x = int(x)
        if sign < 0:
            digits.append(u'-')
        return u''.join(reversed(digits))

    def get_code(self):
        return self.prefix + self._int_to_str(random.randrange(0, self.rand_limit), base=36).zfill(self.rand_len).upper()


if __name__ == '__main__':
    n_codes = 1000  # 生成兑换码个数
    exchange_code = ExchangeCode()
    for x in range(0, n_codes):
        code = exchange_code.get_code()
        print(code)
        # code = GameExchangeCode(code=code_text.upper(), GoldCoin=random.randrange(0, 100), Diamond=random.randrange(0, 100))
        # with app.app_context():
        #     db.session.add(code)
        #     db.session.commit()
