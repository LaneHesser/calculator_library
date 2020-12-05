import calculator


def test_addition():
    assert 4 == calculator.add(2, 2)


def test_subtraction():
    assert 2 == calculator.subtract(4, 2)
