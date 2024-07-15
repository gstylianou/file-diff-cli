import unittest
import os
from main import main


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        file = "test"
        # TESTDATA_FILENAME1 = os.path.join(os.path.dirname(file), "test-file2.txt")
        # print(TESTDATA_FILENAME1)
        main.main(("test-file1.txt", "test-file2.txt"))

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
