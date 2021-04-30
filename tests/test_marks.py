import pytest
import sys


@pytest.mark.skip(reason='Skipped test example')
def test_skip():
    pass


@pytest.mark.skipif(sys.version_info > (4, 5), reason='requires')
def test_skip_if():
    pass


@pytest.mark.xfail(reason='wrong comparison', strict=True)
def test_fail_comparison():
    assert 2 == 4


@pytest.mark.xfail(raises=(AssertionError, TimeoutError))
def test_fail_exception():
    raise AssertionError
