from typing import Dict
from main import Stack


def is_brackets_balanced(s: str) -> str:
    """
    Checks whether the brackets in the input string are balanced.

    A string is considered balanced if:
    - Every opening bracket has a corresponding closing bracket of the same type.
    - Brackets are properly nested and closed in the correct order.

    Supported bracket types: (), {}, []

    Args:
        s (str): The input string containing only bracket characters.

    Returns:
        str: "Сбалансированно" if the string is balanced,
             "Несбалансированно" otherwise.
    """
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches: Dict[str, str] = {')': '(', '}': '{', ']': '['}
    unbalanced = "Несбалансированно"
    balanced = "Сбалансированно"

    for char in s:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return unbalanced
            if stack.pop() != matches[char]:
                return unbalanced

    return balanced if stack.is_empty() else unbalanced


if __name__ == "__main__":
    print(is_brackets_balanced("(((([{}]))))"))                # Сбалансированно
    print(is_brackets_balanced("[([])((([[[]]])))]{()}"))      # Сбалансированно
    print(is_brackets_balanced("{{[()]}}"))                    # Сбалансированно

    print(is_brackets_balanced("}{"))                          # Несбалансированно
    print(is_brackets_balanced("{{[(])]}"))                    # Несбалансированно
    print(is_brackets_balanced("[[{())}]"))                    # Несбалансированно
