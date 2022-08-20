import unittest
from dad_functions import dad_message

class MessageTest(unittest.TestCase):

    def test_hi(self):
        result = dad_message("hi")
        self.assertEqual(False, result)

    def test_Hello(self):
        result = dad_message("Hello")
        self.assertEqual(True, result)

    def test_hello(self):
        result = dad_message("hello")
        self.assertEqual(True, result)

    def test_heLLo(self):
        result = dad_message("heLLo")
        self.assertEqual(True, result)

    def test_gello(self):
        result = dad_message("gello")
        self.assertEqual(False, result)


if __name__=="__main__":
    unittest.main()