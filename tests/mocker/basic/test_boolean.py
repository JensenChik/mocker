from unittest import TestCase
from mocker import Boolean


class TestBoolean(TestCase):

    def testAssertError(self):
        with self.assertRaises(AssertionError):
            Boolean(-1)
        with self.assertRaises(AssertionError):
            Boolean(0)
        with self.assertRaises(AssertionError):
            Boolean(None)

    def testReturnCount(self):
        self.assertEqual(len(Boolean(3)), 3)
        self.assertEqual(len(Boolean(11)), 11)

    def testRatio(self):
        true_count = 0
        for flag in Boolean(12345, true_ratio=0.1):
            true_count += 1 if flag else 0
        self.assertAlmostEqual(1.0 * true_count / 12345, 0.1, 1)
