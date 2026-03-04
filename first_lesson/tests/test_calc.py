import pytest
from calc import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(8, 2) == 4

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)