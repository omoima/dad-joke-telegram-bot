import unittest
from dad_functions import message

class MessageTest(unittest.TestCase):

    def test_hi(self):
        result = message("hi")
        self.assertEqual(False, result)

    def test_Hello(self):
        result = message("Hello")
        self.assertEqual(True, result)

    def test_hello(self):
        result = message("hello")
        self.assertEqual(True, result)

    def test_heLLo(self):
        result = message("heLLo")
        self.assertEqual(True, result)

    def test_gello(self):
        result = message("gello")
        self.assertEqual(False, result)


if __name__=="__main__":
    unittest.main()