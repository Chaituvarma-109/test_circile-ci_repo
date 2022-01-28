import pytest
import main


class Test:
    def test_add(self):
        res = main.add(2, 3)
        assert res == 5

    def test_sub(self):
        res = main.sub(2, 3)
        assert res == 1
        res = main.sub(3, 2)
        assert res == 1

    def test_mul(self):
        res = main.mul(2, 3)
        assert res == 6
