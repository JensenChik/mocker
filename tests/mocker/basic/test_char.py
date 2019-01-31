from unittest import TestCase
from mocker import Char


class TestChar(TestCase):
    def testAssertError(self):
        with self.assertRaises(AssertionError):
            Char(-1)
        with self.assertRaises(AssertionError):
            Char(count=-1)
        with self.assertRaises(AssertionError):
            Char(0)
        with self.assertRaises(AssertionError):
            Char(count=0)
        with self.assertRaises(AssertionError):
            Char('some string')
        with self.assertRaises(AssertionError):
            Char(count='some string')
        with self.assertRaises(AssertionError):
            Char(None)

    def testReturnCount(self):
        self.assertEqual(len(Char(3)), 3)
        self.assertEqual(len(Char(11)), 11)

    def testReturnChar(self):
        pass
