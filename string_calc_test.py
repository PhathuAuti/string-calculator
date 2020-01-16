import  pytest
from string_calculator import add

#  testing empty string returns 0
def test_add_empty_string():
    assert add("") == 0

#  testing addition of positive numbers of any string length
def test_add_positive_integers():
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("1,3,5,9") == 18

# testing to handle the new line characters
def test_add_with_new_lines():
    assert add("1\n2,3") == 6

# testing to support delimiters of any shapes and sizes
def test_add_with_delimiters():
    assert add("//;\n1;2") == 3
    assert add("//***\n1***2***3") == 6
    assert add("//[\*][%]\n1\*2%3") == 6
    assert add("//***//[\*][%]\n1\*2%3\n1***2***3") == 12

#  testing negatives not allowed
def test_add_negative_integers():
    with pytest.raises(Exception) as error:
        assert add("-1,-2,3,4")
    assert str(error.value) == 'ERROR: negatives not allowed -1,-2'

# testing numbers bigger than a 1000
def test_add_bigger_than_thousand():
    assert add("//;\n1000,1;2") == 3




    