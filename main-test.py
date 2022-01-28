from main import add, sub, mul


def Test_add():
    assert add(2, 3) == 5


def Test_sub():
    assert sub(2, 3) == 1
    assert sub(3, 2) == 1


def Test_mul():
    assert mul(2, 3) == 6


if __name__ == "__main__":
    Test_add()
    Test_sub()
    Test_mul()
