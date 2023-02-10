class TestNewFile:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Phrase >= 15 characters"