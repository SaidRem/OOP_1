import unittest
from calc_vote import vote


class TestVoteCalc(unittest.TestCase):
    def test_basic_case(self):
        """Test basic case with clear majority"""
        self.assertEqual(vote(['a', 'b', 'a', 'c', 'a']), 'a')

    def test_single_element(self):
        """Test with single element list"""
        self.assertEqual(vote(['x']), 'x')

    def test_all_unique(self):
        """Test when all elements are unique"""
        self.assertIn(vote(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_tie_case(self):
        """Test when there's a tie for most frequent"""
        result = vote(['a', 'b', 'a', 'b'])
        self.assertIn(result, ['a', 'b'])

    def test_numeric_votes(self):
        """Test with numeric values"""
        self.assertEqual(vote([1, 2, 3, 2, 2, 3, 1, 2]), 2)

    def test_empty_list(self):
        """Test with empty input list"""
        with self.assertRaises(ValueError):
            vote([])

    def test_large_list(self):
        """Test with large input list"""
        votes = ['a'] * 100 + ['b'] * 99 + ['c'] * 50
        self.assertEqual(vote(votes), 'a')

    def test_mixed_types(self):
        """Test with mixed type elements"""
        self.assertEqual(vote([1, '1', 1, '1', 1]), 1)

    def test_boolean_values(self):
        """Test with boolean values"""
        self.assertTrue(vote([True, False, True, True]))

    def test_none_values(self):
        """Test with None values"""
        self.assertIsNone(vote([None, 'a', None, None]))


if __name__ == "__main__":
    unittest.main()
