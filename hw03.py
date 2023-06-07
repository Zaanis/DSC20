"""
DSC 20 Fall 2022 Homework 03
Name: Joshua Chen
PID: A16810747
"""

# Question 1.1
def operate_nums(lst):
    """
    ##############################################################
    check if lst is integers, if not all integers, assertion error
    if all integers, return twice if integer odd, 
    triple if integer is even
    ##############################################################

    >>> operate_nums([1, 2, 3, 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3.1, -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]
    >>> operate_nums([[]])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([0, 1, 2, 3, 4])
    [0, 2, 6, 6, 12]
    >>> operate_nums(['a', 'b'])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    triple = 3
    double = 2
    assert type(lst) == list
    assert all([isinstance(number, int) for number in lst])
    return [value * triple if value % double == 0 else \
    value * double for value in lst]


# Question 1.2
def string_lengths(text, nums):
    """
    ##############################################################
    check for list of non empty string and list of positive integers
    of same length, if not, assertion error
    return list of boolean, True means length greater than integer
    False otherwise
    ##############################################################

    >>> string_lengths(['a', 'b', 'c'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', 'abc'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['a', 'b'], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5])
    [True, False, False]
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5, 6])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde', 'abcdef'], [1, 1, 1, 1])
    [True, True, True, True]
    >>> string_lengths([], [])
    []
    """
    # YOUR CODE GOES HERE #
    assert all([isinstance(letter, str) for letter in text])
    assert all([isinstance(number, int) for number in nums])
    assert type(text) == list and type(nums) == list
    assert len(text) == len(nums)
    assert all(len(letter) > 0 for letter in text)
    assert all(number >= 0 for number in nums)
    return [True if len(text[i]) > nums[i] else False \
    for i in range(len(text))]


# Question 1.3
def process_dict(input_dict):
    """
    ##############################################################
    takes a dictionary, keys are tuples and values are lists of strings
    return a list of integers representing sum of the length of key
    and total length of strings in value
    ##############################################################

    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2, ): ['b']})
    [15, 2]
    >>> process_dict({(1, 2, 3): ['dsc', 'dsc20', 'dsc30'], (2, 1): ['b']})
    [16, 3]
    >>> process_dict({'a': 'hello', 'b': 'goodbye'})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict('hello')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    assert type(input_dict) == dict
    assert all([isinstance(keys, tuple) for keys in list(input_dict.keys())])
    assert all([isinstance(values, str) for keys in list(input_dict.keys()) \
    for values in input_dict.get(keys)])
    assert all([isinstance(values, list) for values in \
    list(input_dict.values())])
    return [len(list(input_dict.keys())[i]) + sum([len(words) for words in \
    list(input_dict.values())[i]]) for i in range(len(input_dict))]


# Question 2
def union(str1, str2):
    """
    ##############################################################
    takes in 2 alphanumeric strings and return union of two strings
    in sorted order, str1[i] and str2[i] belong to the union if 
    str1[i] != str2[i]
    ##############################################################

    >>> union("bbbaabbb", "dddaa")
    'bbbbbbddd'
    >>> union("1234", "156")
    '23456'
    >>> union("ddd", "ddd")
    ''
    >>> union("bbbaabbb", 1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> union("abcdefg", "a bcde")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> union('dddaa', 'bbbaabbb')
    'dddbbbbbb'
    >>> union('12abc', '34def')
    '12abc34def'
    """
    assert type(str1) == str and type(str2) == str
    assert str1.isalnum() and str2.isalnum()
    return "".join([str1[i] if str1[i] != str2[i] else '' \
    for i in range(min(len(str1), len(str2)))] + \
    [str1[i] for i in range(min(len(str1), len(str2)), len(str1))] + \
    [str2[i] if str1[i] != str2[i] else '' \
    for i in range(min(len(str1), len(str2)))] + \
    [str2[i] for i in range(min(len(str1), len(str2)), len(str2))])


# Question 3
def decode(to_decode):
    """
    ##############################################################
    number moved to end and multiplied by 2,
    lowercase characters and spaces stay at same position
    lowercase vowel converted to upper
    upper case nonvowel converted to lower
    ##############################################################

    >>> decode(["3.14IS PIE", "11My aGe iS"])
    ['.Is pIE628', 'my AgE Is22']
    >>> decode(["go t6o sleep at ", "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> decode("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> decode(["3.1415"])
    ['.628210']
    >>> decode(['3.1415', 'hello'])
    ['.628210', 'hEllO']
    >>> decode("abcdefg")
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert all(isinstance(word, str) for word in to_decode) and \
    type(to_decode) == list
    double = 2
    return ["".join([to_decode[list_position][string_position].upper() \
    if to_decode[list_position][string_position] in \
    ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] \
    else "" if to_decode[list_position][string_position].isdigit() \
    else to_decode[list_position][string_position].lower() \
    for string_position in range(len(to_decode[list_position]))] + \
    [str(int(to_decode[list_position][string_position]) * double) \
    if to_decode[list_position][string_position].isdigit() \
    else "" for string_position in range(len(to_decode[list_position]))]) \
     for list_position in range(len(to_decode))]


# Question 4
def rotate_matrix(matrix):
    """
    ##############################################################
    rotate the matrix 90 degrees clockwise
    ##############################################################
    
    >>> rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    >>> rotate_matrix([[1,0,1],[1,0,1],[0,0,0], [1,0,1]])
    [[1, 0, 1, 1], [0, 0, 0, 0], [1, 0, 1, 1]]
    >>> rotate_matrix([[1,1,1,1], [2,2,2,2], [3,3,3,3]])
    [[3, 2, 1], [3, 2, 1], [3, 2, 1], [3, 2, 1]]
    >>> rotate_matrix([[1]])
    [[1]]
    >>> rotate_matrix([[1, 1], [2, 2]])
    [[2, 1], [2, 1]]
    >>> rotate_matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
    [[4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]]
    """
    # YOUR CODE GOES HERE #
    assert all(isinstance(value[i], int) \
    for value in matrix for i in range(len(matrix[0])))
    return [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] \
    for i in range(len(matrix[0]))]

# Question 5.1
def cheapest_gas(gas_stations, mileage):
    """
    ##############################################################
    takes in non-negative integer representing the remaining milage
    of vehicle and dictionary where keys are gas brand name and values
    are list of length 2-tuples representing distance, price
    return brand name with lowest price among reachable stations
    if there is a tie, return any of them
    ##############################################################

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'
    >>> cheapest_gas(gas_stations, 50)
    'Shell'
    >>> gas_stations = { \
        'Shell': [(5, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 1), (60, 5.7)], \
        'Arco': [(5, 5.2), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 5)
    'Arco'
    >>> cheapest_gas(gas_stations, 100)
    'Chevron'
    """
    # YOUR CODE GOES HERE #
    lst1 = [(gas_stations.get(stations)[i][1], stations) \
    for stations in gas_stations \
    for i in range(len(gas_stations.get(stations))) \
    if gas_stations.get(stations)[i][0] <= mileage]
    return min(lst1)[1]


# Question 5.2
def cheapest_average_gas(gas_stations, mileage):
    """
    ##############################################################
    return lowest average price among reachable stations
    ##############################################################

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.1), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 20)
    'Shell'
    >>> cheapest_average_gas(gas_stations, 80)
    'Arco'
    >>> gas_stations = { \
        'Shell': [(5, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.5), (60, 5.7)], \
        'Arco': [(5, 5.2), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Shell'
    >>> cheapest_average_gas(gas_stations, 60)
    'Arco'
    """
    # YOUR CODE GOES HERE #
    return min([(sum([gas_stations.get(stations)[i][1] \
    for i in range(len(gas_stations.get(stations))) \
    if gas_stations.get(stations)[i][0] <=mileage])/len(\
    [gas_stations.get(stations)[i][1] \
    for i in range(len(gas_stations.get(stations))) \
    if gas_stations.get(stations)[i][0] <=mileage]), stations) \
    for stations in gas_stations if len([gas_stations.get(stations)[i][1] \
    for i in range(len(gas_stations.get(stations))) \
    if gas_stations.get(stations)[i][0] <=mileage]) != 0])[1]


# Question 6
def session_money(lst, operations):
    """
    ##############################################################
    define a dictionary of lambda functions, all should return
    list of money after command is applied, 6 possible commands
    1. add, add amount
    2. lose, subtract amount
    3. combine, combine k subsequent number into one
    4. first, take first k digits of number
    5. last, take last k digits of number
    6. reduce_last, replace last k digit of number with thier sum
    ##############################################################

    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('add', 5), ('last', 3), ('reduce_last', 2)]
    >>> session_money(lst, operations_1)
    [6, 17, 128, 239, 811]
    >>> operations_2 = [('first', 3), ('combine', 2), ('lose', 10)]
    >>> session_money(lst, operations_2)
    [3, 125, 236, 236, 236]
    >>> operations_3 = [('first', 3), ('add', 2), ('lose', 2)]
    >>> session_money(lst, operations_3)
    [1, 12, 123, 123, 123, 123]
    >>> operations_4 = [('last', 3), ('first', 2)]
    >>> session_money(lst, operations_4)
    [1, 12, 12, 23, 34, 45]
    >>> operations_5 = [('last', 3), ('first', 2), ('reduce_last', 3)]
    >>> session_money(lst, operations_5)
    [1, 12, 12, 102]
    """
    # TODO: Fill out the lambda functions as dictionary values
    commands = {
        'add': lambda lst, amount: [x + amount for x in lst], 
        'lose': lambda lst, amount: [x - amount for x in lst], 
        'combine': lambda lst, k: [sum([lst[i] for i in range(j, j + k)]) \
        for j in range(len(lst)) if j < len(lst) - k + 1], 
        'first': lambda lst, k: [int(str(lst[i])[0:k]) \
        for i in range(len(lst))], 
        'reduce_last': lambda lst, k: [[lst[i] if i < len(lst) - k \
        else sum([lst[i] for i in range(i, len(lst))]) \
        for i in range(len(lst) - k + 1)] if k !=0 else lst][0], 
        'last': lambda lst, k: [int(str(lst[i])) if k >= len(str(lst[i])) \
        else int((str(lst[i])[len(str(lst[i])) - k::])) \
        for i in range(len(lst))]}
    # YOUR CODE GOES HERE #
    return_list = lst
    for i in range(len(operations)):
        return_list = commands[operations[i][0]](return_list, operations[i][1])
    return return_list