from calculator import add, sub, mul, div
from pytest import raises


def test_add():
    assert add(0, 5) == 5
    assert add(-2, 3) == 1
    assert add(100, 50) == 150



def test_sub():
    assert sub(0, 5) == -5
    assert sub(-2, 3) == -5
    assert sub(100, 50) == 50


def test_mul():
    assert mul(0, 5) == 0
    assert mul(-2, 3) == -6
    assert mul(100, 50) == 5000


def test_div():
    assert div(10, 2) == 5.0
    with raises(ZeroDivisionError):
        div(5, 0)