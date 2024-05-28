from fuel import convert, gauge
import pytest


def test_gauge():
    assert gauge(99) == 'F'