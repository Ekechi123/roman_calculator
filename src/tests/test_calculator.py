import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from main import calculate

def test_roman_to_arabic():
    result = calculate("(VII + V) * II + I")
    assert result == "XXV" 

def test_addition():
    result = calculate("VII + V")
    assert result == "XII" 

def test_subtraction():
    result = calculate("X - III")
    assert result == "VII"  

def test_multiplication():
    result = calculate("VI * III")
    assert result == "XVIII"  

def test_division():
    result = calculate("X / II")
    assert result == "V"  

def test_invalid_input():
    result = calculate("VII + !")
    assert result == "I don’t know how to read this."  
