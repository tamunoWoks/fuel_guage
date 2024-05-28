from fuel import convert, gauge
import pytest


def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(23) == '23%'