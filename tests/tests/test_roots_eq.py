import unittest
from calc_roots_eq import solution


class TestRootsEq(unittest.TestCase):

    def test_no_roots(self):
        res = solution(1, 1, 1)
        self.assertEqual("корней нет", res)

    def test_negative_roots(self):
        res = solution(1, 8, 15)
        self.assertTupleEqual(res, (-3.0, -5.0))

    def test_pos_roots(self):
        res = solution(1, -13, 12)
        self.assertTupleEqual(res, (12.0, 1.0))

    def test_one_root(self):
        res = solution(-4, 28, -49)
        self.assertEqual(res, 3.5)


if __name__ == "__main__":
    unittest.main()
