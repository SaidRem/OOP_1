import pytest
from brackets import is_brackets_balanced


@pytest.mark.parametrize("input_str, expected", [
    ("(((([{}]))))", "Сбалансированно"),
    ("[([])((([[[]]])))]{()}", "Сбалансированно"),
    ("{{[()]}}", "Сбалансированно"),
    ("}{", "Несбалансированно"),
    ("{{[(])]}}", "Несбалансированно"),
    ("[[{())}]", "Несбалансированно"),
    ("", "Сбалансированно"),
    ("{[}", "Несбалансированно"),
    ("((()))", "Сбалансированно"),
    ("([{}])", "Сбалансированно"),
    ("([)", "Несбалансированно"),
])
def test_is_brackets_balanced(input_str, expected):
    assert is_brackets_balanced(input_str) == expected
