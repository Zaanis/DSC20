"""
DSC 20 Lab 06
Name: Joshua Chen
PID: A16810747
"""

# Problem 1
def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function.
    You don't need to add new doctests for this function.
    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [False, False, False, True, False, True, False, True, False, True]


# Problem 2
def prerequisites(*args, **kwargs):
    """
    Returns a list of people who have completed the prerequisites
    >>> prerequisites('DSC30', 'DSC40A',\
                      Marina = ['DSC10', 'DSC20', 'DSC30', 'DSC40A'], \
                      Bryce = ['DSC10', 'DSC20', 'ECE35', 'CSE30'], \
                      Mishari = ['DSC10', 'DSC20', 'DSC30'])
    ['Marina']
    >>> prerequisites('DSC10',\
                      Marina = ['DSC10', 'DSC20', 'DSC30', 'DSC40A'], \
                      Bryce = ['DSC10', 'DSC20', 'ECE35', 'CSE30'])
    ['Marina', 'Bryce']
    >>> prerequisites('CSE30',\
                      Marina = ['DSC10', 'DSC20', 'DSC30', 'DSC40A'], \
                      Bryce = ['DSC10', 'DSC20', 'ECE35', 'CSE30'], \
                      Mishari = ['DSC10', 'DSC20', 'DSC30'],\
                      Ella = ['DSC10', 'DSC20', 'DSC30'])
    ['Bryce']
    """
    return_list = []
    for i in args:
        for k in kwargs:
            if i in kwargs.get(k):
                if k not in return_list:
                    return_list.append(k)
            else:
                if k in return_list:
                    return_list.remove(k)
    return return_list


# Problem 3
def building_mats(*args, **kwargs):
    """
    Returns a list of blocks that are not enough in supply
    >>> building_mats(('oak_log', 16), ('oak_log', 32), oak_log=35)
    []
    >>> building_mats(('oak_log', 16), ('oak_log', 32), oak_log=50)
    ['oak_log']
    >>> building_mats(('oak_log', 55), ('oak_plank', 600), ('glass', 44),\
                      ('oak_slab', 60), ('glass', 20), ('glass', 24),\
                      oak_log=64, oak_stair=48, oak_plank=400, glass=64)
    ['oak_log', 'oak_stair']
    """
    supply = {}
    for i in args:
        if i[0] not in supply:
            supply[i[0]] = i[1]
        else:
            supply[i[0]] += i[1]
    return_list = []
    for k in kwargs:
        if k not in supply:
            return_list.append(k)
        elif kwargs[k] > supply[k]:
            return_list.append(k)
    return return_list


# Problem 4.1
def reverse_str(name):
    """
    Recursively reverses the string
    >>> reverse_str("aniraM")
    'Marina'
    >>> reverse_str("retsnoM yracS")
    'Scary Monster'
    >>> reverse_str("dneirFnogarD")
    'DragonFriend'
    """
    if len(name) == 0:
        return name
    else:
        return reverse_str(name[1:]) + name[0]


# Problem 4.2
def reverse_list(lst):
    """
    Recursively Reverses each string in the list

    >>> reverse_list(["aniraM", "irahsiM",  "ecyrB"])
    ['Marina', 'Mishari', 'Bryce']
    >>> reverse_list(["retsnoM yracS", 'dneirFnogarD'])
    ['Scary Monster', 'DragonFriend']
    >>> reverse_list([])
    []
    """
    if len(lst) == 0:
        return lst
    else:
        return reverse_list(lst[:-1]) + [reverse_str(lst[-1])]

# Problem 5
def remove_dragon(lst):
    """
    Recursively return a new list where strings with dragon are removed
    
    >>> remove_dragon(["Black Dragon", "Amy", "Johnny dragon", "Amir"])
    ['Amy', 'Amir']
    >>> remove_dragon(["Black Dragon", "White Dragon", "Blue Dragon"])
    []
    >>> remove_dragon(["Samira", "Malakai", "Purple Flame"])
    ['Samira', 'Malakai', 'Purple Flame']
    """
    if len(lst) == 0:
        return []
    if lst[0].lower().count('dragon') > 0:
        return [] + remove_dragon(lst[1:])
    else:
        return [lst[0]] + remove_dragon(lst[1:])


# Problem 6
def sum_odd(lst):
    """
    Recursively sums all odd numbers in the list
    >>> sum_odd([1,2,3,4,5,6])
    9
    >>> sum_odd([1,1,1,1,1])
    5
    >>> sum_odd([1,2,3,4,2])
    4
    """
    if len(lst) == 0:
        return 0
    if lst[0] % 2 == 1:
        return lst[0] + sum_odd(lst[1:])
    elif lst[0] % 2 == 0:
        return sum_odd(lst[1:])


# Problem 7
def duplication_glitch(num_diamonds, hours):
    """
    Recursively counts the number of diamonds that can be duplicated
    >>> duplication_glitch(2, 4)
    32
    >>> duplication_glitch(3, 5)
    96
    >>> duplication_glitch(256, 2)
    1024
    """
    if hours == 0:
        return num_diamonds
    else:
        return num_diamonds * 2 ** (hours-1) + \
        duplication_glitch(num_diamonds, hours-1)