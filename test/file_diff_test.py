import unittest
from lib.file_diff import FileDiff


class TestSum(unittest.TestCase):
    def test_sum(self):
        print("running test...")
        calculator = FileDiff()
        self.assertEqual(calculator.add(1, 2), 3)

    # if __name__ == "__main__":
    #     unittest.main()
