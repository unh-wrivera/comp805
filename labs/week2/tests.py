"""
Author: William Rivera
Assignment: UNHM COMP705/805 Lab 2
Title: Testing Python Practice Functions
Date: 11 February 2018
"""

import lab2

#Test Cases:
list1 = [1, 2, 3]
list2 = []
list3 = [-1, -2, -3]
list4 = [1, 0]

def test_squared_nums():
    """
    Checks if squared_nums() function works when tested using provided test cases.
    """
    print("")
    print("Testing lab2.test_squared_nums()")
    print("...")
    print("Test Case No. 1:{}".format(list1))
    print("Expected Output:[1, 4, 9]")
    print("Actual Output:{}".format(lab2.squared_nums(list1)))


    print("")
    print("Testing lab2.test_squared_nums()")
    print("...")
    print("Test Case No. 2:{}".format(list2))
    print("Expected Output:[]")
    print("Actual Output:{}".format(lab2.squared_nums(list2)))


    print("")
    print("Testing lab2.test_squared_nums()")
    print("...")
    print("Test Case No. 3:{}".format(list3))
    print("Expected Output:[1, 4, 9]")
    print("Actual Output:{}".format(lab2.squared_nums(list3)))


    print("")
    print("Testing lab2.test_squared_nums()")
    print("...")
    print("Test Case No. 4:{}".format(list4))
    print("Expected Output:[1, 0]")
    print("Actual Output:{}".format(lab2.squared_nums(list4)))

#Test Case:
movie_list1 = ['Hello World', 'Hello_world', 'Title']
movie_list2 = ['Hello_World', 'A great 3 Days', 'hello World']
movie_list3 = ['10, 11, 12']
movie_list = movie_list1+movie_list2+movie_list3

def test_check_title():
    """
    Checks to see if check_title() function correctly removes,
    non 'title case' titles and titles including numbers from title list.
	"""

    print("")
    print("Testing lab2.test_check_title()")
    print("...")
    print("Test Case:{}".format(movie_list))
    print("Expected Output: ['Hello World', 'Title'], [], []")
    print("Actual Output:{}".format(lab2.check_title(movie_list)))



#Test Cases:
d1 = {'pencil':10, 'pen':8, 'paper':7}
d2 = {'pencil':0, 'pen':-3, 'paper':-11}
d3 = {'pencil':0.5, 'pen':-3.2, 'paper':11.0}


def test_restock_inventory():
    """
    Tests restock_inventory to ensure it adds correct amount of supplies to inventories (i.e., dictionaries) provided.
    """
    print("")
    print("Testing lab2.test_restock_inventory()")
    print("...")
    print("Test Case No.1:{}".format(d1))
    print("Expected Output: {'pencil':20, 'pen':18, 'paper':17}")
    print("Actual Output:{}".format(lab2.restock_inventory(d1)))

    print("")
    print("Testing lab2.test_restock_inventory()")
    print("...")
    print("Test Case No.2 :{}".format(d2))
    print("Expected Output: {'pencil':10, 'pen':7, 'paper':-1}")
    print("Actual Output:{}".format(lab2.restock_inventory(d2)))

    print("")
    print("Testing lab2.test_restock_inventory()")
    print("...")
    print("Test Case No.3:{}".format(d3))
    print("Expected Output: {'pencil':10.5, 'pen':6.8, 'paper':21.0}")
    print("Actual Output:{}".format(lab2.restock_inventory(d3)))

dict1 = {'pencil':10, 'pen':8, 'paper':7} 
dict2 = {'pencil':0, 'pen':-3, 'paper':-11}
dict3 = {'pencil':0.5, 'pen':-3.2, 'paper':0.0}


def test_filter_0_items():
    """
    Tests filter_0_items function to ensure values equal to 0 are removed from the dictionary.
    """
    print("")
    print("Testing lab2.filter_0_items()")
    print("...")
    print("Test Case No.1:{}".format(dict1))
    print("Expected Output: {'pen':8, 'paper':7, 'pencil':10}")
    print("Actual Output:{}".format(lab2.filter_0_items(dict1)))


    print("")
    print("Testing lab2.filter_0_items()")
    print("...")
    print("Test Case No.2 :{}".format(dict2))
    print("Expected Output: {'pen':-3, 'paper':-11}")
    print("Actual Output:{}".format(lab2.filter_0_items(dict2)))

    print("")
    print("Testing lab2.filter_0_items()")
    print("...")
    print("Test Case No.3 :{}".format(dict3))
    print("Expected Output: {'pen':-3.2, 'pencil':0.5}")
    print("Actual Output:{}".format(lab2.filter_0_items(dict3)))


#Test Cases:
grade_set1 = {'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}
grade_set2 = {'Michael' :[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}
grade_set3 = {'Michael' :[78], 'Daniel':[90], 'Josh':[900/-9]}

def test_average_grades():
    print("")
    print("Testing lab2.average_grades()")
    print("...")
    print("Test Case No.1 :{}".format(grade_set1))
    print("Expected Output: {'Josh' : 87.0, 'Daniel': 79.0, 'Michael': 89.0}")
    print("Actual Output:{}".format(lab2.average_grades(grade_set1)))

    print("")
    print("Testing lab2.average_grades()")
    print("...")
    print("Test Case No.2 :{}".format(grade_set2))
    print("Expected Output: {'Josh' : 88.5, 'Daniel': 52.6625, 'Michael': 94.0}")
    print("Actual Output:{}".format(lab2.average_grades(grade_set2)))

    print("")
    print("Testing lab2.average_grades()")
    print("...")
    print("Test Case No.3 :{}".format(grade_set3))
    print("Expected Output: {'Josh' : -100.0, 'Daniel': 90.0, 'Michael': 78.0}")
    print("Actual Output:{}".format(lab2.average_grades(grade_set3)))