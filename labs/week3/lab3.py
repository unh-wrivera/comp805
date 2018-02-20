"""
Author: William Rivera
Assignment: UNHM COMP705/805 Lab 2
Title: Python Practice
Date: 11 February 2018
"""



#1 Function Interface:

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared

    >>> squared_nums([1, 2, 3])
    [1, 4, 9]
    >>> squared_nums([])
    []
    >>> squared_nums([-1, -2])
    [1, 4]
    """
    return [num**2 for num in num_list]


    #using list comprehension, generate and return list of squared numbers

#What the Function Does:
#Each number in the list will be squared to create a new  return list of squared numbers

#What the Function Does:
#Each number in the list will be squared to create a new list of squared numbers

#Test Cases:list of squared numbers

#Test Cases:
#[1, 2, 3], [], [-1, -2, -3], [1, 0]

#Expected Results:
#[1, 4, 9], [], [1, 4, 9], [1, 0]


#2 Function Interface:

def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    
    >>> check_title(['Hello World', 'Hello_world', 'Title'])
    ['Hello World', 'Title']
    >>> check_title(['Hello_World', 'A great 3 Days', 'hello World'])
    []
    >>> check_title(['10,11,12'])
    []

    """
    truncated_list = []
    for title in title_list:
        if title.istitle() and not any(char.isdigit() for char in title_list):
            truncated_list.append(title)
            for flick in truncated_list:
            	if '_' in flick:
            		truncated_list.remove(flick)
    return truncated_list



#What the Function Does:
#Each string in the list that has numbers and isn’t in title case is removed to create a new string
#Test Cases:
#['Hello World', 'Hello_world', 'Title'], 
#['Hello_World', 'A great 3 Days', 'hello World'], [‘10, 11, 12’]

#Expected Results:
#['Hello World', 'Title'], [], []


#3 **Function Interface:
def restock_inventory(inventory):
    new_inventory = {}
    for key, value in inventory.items():
        new_val = value + 10
        new_inventory[key] = new_val
    return new_inventory
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
       key: string that is the name of the inventory item
       value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked
    """

#What the Function Does:
#Updates a dictionary that keeps track of an inventory, in order to increase the amount of items on record

#Test Cases:
#{'pencil':10, 'pen':8, 'paper':7}, {'pencil':0, 'pen':-3, 'paper':-11}, 
#{'pencil':0.5, 'pen':-3.2, 'paper':11.0}

#Expected Results:
#{'pencil':20, 'pen':18, 'paper':17}, 
#{'pencil':10, 'pen':7, 'paper':-1}, 
#{'pencil':10.5, 'pen':6.8, 'paper':21.0}

#Actual Results:
#{'pen':18, 'paper':17, 'pencil':20}, 
#{'pen':7, 'paper':-1, 'pencil':10}, 
#{'pen':6.8, 'paper':21.0, 'pencil':10.5}


#4 Function Interface:
def filter_0_items(inventory):

    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
       key: tring that is the name of the inventory item
       value: nteger that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed

    """
    return_dict = {}
    for key, value in inventory.items():
        if inventory[key] !=0:
            return_dict[key] = inventory[key]
    return return_dict

#What the Function Does:
#Updates the dictionary so that all items that their are currently none of are removed from the dictionary

#Test Cases:
#{'pencil':10, 'pen':8, 'paper':7}, {'pencil':0, 'pen':-3, 'paper':-11}, 
#{'pencil':0.5, 'pen':-3.2, 'paper':0.0}

#Expected Results:
#{'pen':8, 'paper':7, 'pencil':10}, {'pen':-3, 'paper':-11}, 
#{'pen':-3.2, 'pencil':0.5}




#5 **Function Interface:
def average_grades(grades):

    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    new_grades = { }
    for student_name, student_grades in grades.items( ):
        new_grades[student_name] = sum(student_grades) / len(student_grades)
    return new_grades

#What the Function Does:
#Changes the dictionary so each student has one average grade associated with them rather than a list of grades

#Test Cases:
#{'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}, 
#{'Michael' :[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0] 'Josh':[99 + 1 * -2, 40/.5]}, 
#{'Michael' :[78], 'Daniel':[90], 'Josh':[900/-9]}

#Expected Results:
#{'Josh' : 87.0, 'Daniel': 79.0, 'Michael': 89.0},
#{'Josh' : 88.5, 'Daniel': 52.6625, 'Michael': 94.0},
#{'Josh' : -100.0, 'Daniel': 90.0, 'Michael': 78.0}

if __name__ == '__main__':
    import doctest
    doctest.testmod()