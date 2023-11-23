import pytest
from function1 import addition, subtraction 

def test_addition():
    assert addition(4, 3) == 7
    assert addition(0, 0) == 0
    assert addition(-1, 1) == 0  

def test_subtraction():
    assert subtraction(4, 3) == 1
    assert subtraction(0, 0) == 0
    assert subtraction(5, -3) == 8  
    assert subtraction(-1, 1) == -2