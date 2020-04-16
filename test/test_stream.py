import pytest
from karen import stream

s = stream.Stream("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789!@#$%*()_-+=")


@pytest.mark.stream
def test_read():
    assert s.read()


@pytest.mark.stream
def test_get_ratio():
    assert False


@pytest.mark.stream
def test_get_frecuency():
    assert False


def test_get_ramp():
    assert False


def test_to_list():
    assert False


