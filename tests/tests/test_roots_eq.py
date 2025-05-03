import unittest
from calc_roots_eq import solution


class TestRootsEq(unittest.TestCase):
    # test_cases = [
    #     [(1, 8, 15), (-3.0, -5.0)],
    #     [(1, -13, 12), (12.0, 1.0)],
    #     [(-4, 28, -49), 3.5],
    #     [(1, 1, 1), "корней нет")],
    #     [(1, 2, 2), "fuck"]
    # ]

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


    # def test_all(self):
    #     for args, res_right in self.test_cases:
    #         with self.subTest(args=args):
    #             res = solution(*args)
    #             self.assertEqual(res_right, res)

if __name__ == "__main__":
    unittest.main()
