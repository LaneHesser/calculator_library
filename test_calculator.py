import calculator


def test_addition():
    assert 4 == calculator.add(2, 2)


def test_subtraction():
    assert 2 == calculator.subtract(4, 2)


def test_multiplication():
    assert 100 == calculator.multiply(10, 10)


def test_division():
    assert 10.0 == calculator.division(100, 10)
