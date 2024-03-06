from fuel import convert, gauge
import pytest


def main():
    test_correct_input()
    test_value()
    test_zeros_division()


def test_zeros_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value():
    with pytest.raises(ValueError):
        convert("cat")


def test_correct_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/1") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"


if __name__ == "__main__":
    main()
