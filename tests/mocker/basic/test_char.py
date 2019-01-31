from unittest import TestCase
from mocker import Char
from dictionary import ALPHABET


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

    def testReturnCharInSelection(self):
        for char in Char(1000):
            self.assertTrue(char in ALPHABET)

        selection = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for char in Char(1000, selection=selection):
            self.assertTrue(char in selection)

    def testRatio(self):
        char_count = dict([(char, 0) for char in ALPHABET])
        for char in Char(100000):
            char_count[char] += 1
        for count in char_count.values():
            self.assertAlmostEqual(1.0 * count / 100000, 1.0 / 52, 2)

        selection = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        char_count = dict([(char, 0) for char in selection])
        for char in Char(100000, selection=selection):
            char_count[char] += 1
        for count in char_count.values():
            self.assertAlmostEqual(1.0 * count / 100000, 0.1, 2)
