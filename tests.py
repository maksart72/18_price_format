from unittest import TestCase
from format_price import format_price

class TestFormat_price(TestCase):

    def test1(self):
        price = format_price(0)
        self.assertEqual(price, '0.00')

    def test2(self):
        price = format_price(1000)
        self.assertEqual(price, '1 000.00')

    def test3(self):
        price = format_price(1000.999)
        self.assertEqual(price, '1 001.00')

    def test4(self):
        price = format_price(1000.000099)
        self.assertEqual(price, '1 000.00')

    def test5(self):
            price = format_price(1000.)
            self.assertEqual(price, '1 000.00')

    def test6(self):
            price = format_price(1000000)
            self.assertEqual(price, '1 000 000.00')

    def test7(self):
            price = format_price(00.00)
            self.assertEqual(price, '0.00')

    def test8(self):
            price = format_price(000.1000)
            self.assertEqual(price, '0.10')

    def test9(self):
            price = format_price(.777)
            self.assertEqual(price, '0.78')

    def test10(self):
        price = format_price(-10)
        self.assertEqual(price, None)

    def test11(self):
        price = format_price('abc')
        self.assertEqual(price, None)


if __name__ == '__main__':
    unittest.main()
