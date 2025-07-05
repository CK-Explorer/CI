import pytest

from package.main import addition


@pytest.mark.parametrize("a, b, c", [
    (5, 6, 11),
    (10, 8, 18),
    (1, 1, 2)
])
def test_addition(a, b, c):
    assert c == addition(a,b)
