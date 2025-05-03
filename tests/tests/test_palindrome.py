import unittest
from palindrome import palindrome_calc


class TestPalindromeCalc(unittest.TestCase):
    def test_single_palindrome(self):
        """Test with a single palindrome phrase"""
        phrases = ["madam"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, ["madam"])

    def test_multiple_palindromes(self):
        """Test with multiple palindrome phrases"""
        phrases = ["racecar", "hello", "noon", "world"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, ["racecar", "noon"])

    def test_empty_list(self):
        """Test with an empty input list"""
        phrases = []
        result = palindrome_calc(phrases)
        self.assertEqual(result, [])

    def test_no_palindromes(self):
        """Test when no phrases are palindromes"""
        phrases = ["python", "testing", "unittest"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, [])

    def test_mixed_case_palindromes(self):
        """Test case-insensitive palindromes (should fail as function is case-sensitive)"""
        phrases = ["Madam", "RaceCar", "NoOn"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, [])  # Expect empty because function is case-sensitive

    def test_palindromes_with_spaces(self):
        """Test phrases with spaces that are palindromes when spaces are removed"""
        phrases = ["a man a plan a canal panama", "never odd or even", "not a palindrome"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, ["a man a plan a canal panama", "never odd or even"])

    def test_palindromes_with_punctuation(self):
        """Test phrases with punctuation (should fail as function doesn't handle punctuation)"""
        phrases = ["A man, a plan, a canal: Panama!", "Was it a car or a cat I saw?"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, [])  # Expect empty because function doesn't handle punctuation

    def test_numeric_palindromes(self):
        """Test numeric palindromes as strings"""
        phrases = ["12321", "123", "1 2 3 2 1"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, ["12321", "1 2 3 2 1"])

    def test_single_character(self):
        """Test single character phrases (all are palindromes)"""
        phrases = ["a", "b", "c"]
        result = palindrome_calc(phrases)
        self.assertEqual(result, ["a", "b", "c"])

    def test_empty_string(self):
        """Test empty string in input"""
        phrases = [""]
        result = palindrome_calc(phrases)
        self.assertEqual(result, [""])

if __name__ == '__main__':
    unittest.main()
