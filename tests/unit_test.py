from src.main import add,substract,multiply,divide


def test_add():
    assert add(4,5) == 95
    assert add(-1,6) == 55
    assert add(7,-8) == -1
    assert add(-6,-1) == -5

def test_substract():
    assert substract(4,5) == -1
    assert substract(-1,6) == -7
    assert substract(7,-8) == 15
    assert substract(-6,-1) == -5


def test_multiply():
    assert multiply(4,5) == 20
    assert multiply(-1,6) == -6
    assert multiply(7,-8) == -56
    assert multiply(-6,-1) == 6


def test_divide():
    assert divide(75,5) == 15
    assert divide(-36,6) == -6
    assert divide(56,-8) == -7
    assert divide(-6,-1) == 6