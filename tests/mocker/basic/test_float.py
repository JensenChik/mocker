from unittest import TestCase
from mocker import Float


class TestFloat(TestCase):
    def testAssertError(self):
        with self.assertRaises(AssertionError):
            Float(-1)
        with self.assertRaises(AssertionError):
            Float(count=-1)
        with self.assertRaises(AssertionError):
            Float(0)
        with self.assertRaises(AssertionError):
            Float(count=0)
        with self.assertRaises(AssertionError):
            Float('some string')
        with self.assertRaises(AssertionError):
            Float(count='some string')
        with self.assertRaises(AssertionError):
            Float(None)

    def test_Float(self):
        self.fail()
