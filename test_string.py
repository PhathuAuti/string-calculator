import string

def test_add_empty_string():
    assert calculator.add(" ") == 0

def test_add_single_input():
    assert calculator.add("1") == 0

def test_add_two_inputs():
    assert calculator.add("1", "2") == 0