from main import Stack


def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    assert not s.is_empty()
    assert s.peek() == 1
    assert s.size() == 1
    assert s.pop() == 1
    assert s.is_empty()
