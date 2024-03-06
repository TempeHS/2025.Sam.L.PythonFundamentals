from bank import value


def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()


def test_return_zero():
    assert value(" ") == 0
    assert value("Hey") == 0
    assert value("Hello Tom") == 0
    assert value("1 2 3 Hello") == 0


def test_return_twenty():
    assert value("Hi") == 20
    assert value("Hi how are you") == 20
    assert value("Hi!") == 20


def test_return_hundred():
    assert value("Nice to see") == 100
    assert value(" Hey how are you") == 100
    assert value("What is your problem!") == 100
