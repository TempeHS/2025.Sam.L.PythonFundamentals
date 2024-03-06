from plates import is_valid


def main():
    test_is_a_letter()
    test_is_end_with_number()
    test_len_second_is_a_letter()


def test_is_a_letter():
    assert is_valid("CS") == True
    assert is_valid("TTTT") == True
    assert is_valid("CS50") == False


def test_is_end_with_number():
    assert is_valid("CS50") == True
    assert is_valid("ABC555") == True


def test_len_second_is_a_letter():
    assert is_valid("T5") == False
    assert is_valid("TSTTTAV") == False
    assert is_valid("A6BCDEF") == False
