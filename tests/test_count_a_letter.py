from main import count_a_letter
import pytest

# def test_demo_one():
#     num_1 = 8
#     num_2 = 9

#     result = num_1 + num_2

#     assert result == 17

# def test_demo_two():
#     num_1 = 18
#     num_2 = 24

#     result = num_1 + num_2

#     assert result == 42
# # Delete the demo tests and add your tests here 


# 1) if string
# 2) if expected
def test_count_a_letter_and_return_expected():
    sentence = 'happy birthday'
    letter = 'a'

    result = count_a_letter('happy birthday', 'a')

    assert result == 2

def test_if_sentence_and_letter_are_empty():

    sentence = ''
    letter = ''

    result = count_a_letter('', '')
    
    assert result == None

def test_for_case_sensitivty():
    pass

def test_if_sentence_and_letter_are_strings():
    pass
