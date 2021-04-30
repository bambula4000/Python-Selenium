import pytest


def num_sign(a):
    if a < 0:
        return 'num_negative'
    elif a > 0:
        return 'num_positive'
    else:
        return 'num_zero'


def test_negative():
    assert num_sign(-1) == 'num_negative'


def test_zero():
    assert num_sign(0) == 'num_zero'


def test_positive():
    assert num_sign(2) == 'num_positive'


@pytest.mark.parametrize('num, result', [
    (-1, 'num_negative'),
    (0, 'num_zero'),
    (2, 'num_positive')
])
def test_all_cases(num, result):
    assert num_sign(num) == result


@pytest.mark.parametrize('a', [1, 2])
@pytest.mark.parametrize('b', [3, 4])
def test_intersect(a, b):
    print(a, b)
