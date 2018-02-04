"""
William Rivera
UNHM COMP705/805 Lab 1
An Introduction to Python
3 February 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string(): 
    """
    This function returns a string value
    """
    s = "This is a string."
    return s

def give_me_an_integer():
    """
    This function returns an integer value
    """
    x =5
    return x

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    isTrue = True
    return isTrue

def give_me_a_float():
    """
    This function returns a float value
    """
    pi = 3.14
    return pi

def give_me_a_list():
    """
    This function returns a list
    """
    collection = [1,'two',3.0]
    return collection

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    pokedex = {001:'Bulbasaur', 151:'Mew'}
    return pokedex

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    tuple1 = ('value1', 'value2',0,1)
    return tuple1

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    sum = 0
    for i in range(11):
    	sum = sum + i
    return sum


def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if number % 2 ==0:
    	return True

    else:
    	return False

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1 < number2:
    	return True

    else:
    	return False

