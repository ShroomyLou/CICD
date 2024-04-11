import pytest
from iseven import is_even

@pytest.mark.parametrize("num, expected_result", [
    (0, 'even'),
    (1, 'odd'),
    (2, 'even'),
    (3, 'odd'),
    (4, 'even')
])
def test_is_even(num, expected_result):
    assert is_even(num) == expected_result


