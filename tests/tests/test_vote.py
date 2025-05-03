import unittest
from calc_vote import vote


class TestVoteCalc(unittest.TestCase):
    # Parametrized test for basic cases
    def test_basic_cases(self):
        test_cases = [
            (['a', 'b', 'a', 'c', 'a'], 'a'),  # Clear winner
            ([1, 2, 2, 2, 3, 3, 3, 2], 2),     # Numeric values
            (['x'], 'x'),                      # Single element
        ]

        for votes, expected in test_cases:
            with self.subTest(votes=votes, expected=expected):
                self.assertEqual(vote(votes), expected)

    # Parametrized test for tie cases
    def test_tie_cases(self):
        test_cases = [
            (['a', 'b', 'a', 'b'], ['a', 'b']),
            ([1, 2, 3, 1, 2, 3], [1, 2, 3]),
            (['cat', 'dog'], ['cat', 'dog']),
        ]

        for votes, possible_results in test_cases:
            with self.subTest(votes=votes):
                result = vote(votes)
                self.assertIn(result, possible_results)

    # Parametrized test for edge cases
    def test_edge_cases(self):
        test_cases = [
            ([], ValueError),                  # Empty list
            (['', '', 'a'], ''),               # Empty strings
            ([1, '1', 1], 1),                  # Mixed types
        ]

        for votes, expected in test_cases:
            with self.subTest(votes=votes, expected=expected):
                if expected is ValueError:
                    with self.assertRaises(ValueError):
                        vote(votes)
                else:
                    self.assertEqual(vote(votes), expected)


if __name__ == "__main__":
    unittest.main()
