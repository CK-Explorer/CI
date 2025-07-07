import pytest

from package.main import addition, subtraction


@pytest.mark.parametrize("a, b, c", [
    (5, 6, 11),
    (10, 8, 18),
    (1, 1, 2)
])
def test_addition(a: int, b: int, c: int) -> None:
    assert c == addition(a,b)

@pytest.mark.parametrize("a, b, c", [
    (5, 6, -1),
    (10, 8, 2),
    (1, 1, 0)
])
def test_subtraction(a: int, b: int, c: int) -> None:
    assert c == subtraction(a,b)
