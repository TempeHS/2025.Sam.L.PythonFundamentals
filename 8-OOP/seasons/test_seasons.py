import pytest
from seasons import date_validate, add_text


def main():
    correct_date_format()
    convert_number()


def correct_date_format():
    with pytest.raises(ValueError):
        date_validate("12/12/2020")
        date_validate("2022/13/1")
        date_validate("2007/12/01")


def convert_number():
    assert (
        add_text("525600") == "Five hundred twenty-five thousand, six hundred minutes"
    )


main()
