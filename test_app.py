# to install in terminal --> pip install pytest
# to run in terminal --> pytest
from app import add, subtract, multiply, divide


# ----------------------
# add
# ----------------------

def test_add():
    assert add(2, 3) == 5
    assert add(5, 0) == 5
    assert add(2, 2) == 4


# ----------------------
# subtract
# ----------------------

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 8) == -4
    assert subtract(1, 1) == 0


# ----------------------
# multiply
# ----------------------

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2, 2) == 4
    assert multiply(5, -5) == -25


# ----------------------
# divide
# ----------------------

def test_divide():
    assert divide(10, 2) == 5
    # Add to this test 


# ----------------------
# exponents
# ----------------------

# Add this test after fixing test_divide
# def test_power():
#     assert power(5, 2) == 25