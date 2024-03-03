import twttr


def test_shorten():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("TWITTER") == "twttr"
    assert twttr.shorten("TwITTer") == "twttr"
    assert twttr.shorten("1234") == "1234"


def test_main():
    with pytest.raises(SystemExit):
        sys.argv = ["", "twitter"]
        twttr.main(None)
