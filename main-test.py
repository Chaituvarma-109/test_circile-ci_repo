from main import add, sub, mul


class Test:
    def test_add(self):
        assert add(2, 3) == 5

    def test_sub(self):
        assert sub(2, 3) == 1
        assert sub(3, 2) == 1

    def test_mul(self):
        assert mul(2, 3) == 6
