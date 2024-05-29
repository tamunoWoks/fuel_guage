from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(23) == '23%'

def test_convert():
    assert convert('1/4') == 25
    assert convert('1/2') == 50

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('5/4')
        convert("cat/dog")