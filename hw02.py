"""
DSC 20 Homework 02
Name: Joshua Chen   
PID: A16810747
"""

# Question 1
def combine(states, nicknames):
    """
    ##############################################################
    take 2 list, list of state and list of corresponding nickname
    return list of tuple, each tuple contain state as first element,
    corresponding nickname as second element, return empty list
    if no nicknames, return empty list
    ##############################################################

    >>> combine(['NV', 'CA', 'HI'], \
    ['Silver State', 'Golden State', 'Aloha State'])
    [('NV', 'Silver State'), ('CA', 'Golden State'), ('HI', 'Aloha State')]

    >>> combine(['NV', 'CA'], ['Silver State', 'Golden State', 'Aloha State'])
    [('NV', 'Silver State'), ('CA', 'Golden State'), \
('NO STATE PROVIDED', 'Aloha State')]

    >>> combine([], ['Golden State', 'Aloha State'])
    [('NO STATE PROVIDED', 'Golden State'), \
('NO STATE PROVIDED', 'Aloha State')]

    # Add at least 3 doctests below here #
    >>> combine(['CA'], [])
    []
    
    >>> combine(['C', 'D'], ['Cows', 'Donkeys'])
    [('C', 'Cows'), ('D', 'Donkeys')]
    
    >>> combine(['NV', 'NV'], ['Silver State', 'Silver State', 'Bronze State'])
    [('NV', 'Silver State'), ('NV', 'Silver State'), \
('NO STATE PROVIDED', 'Bronze State')]
    """
    return_list = []
    for i in range(len(nicknames)):
        if i < len(states):
            return_list.append((states[i], nicknames[i]))
        elif i >= len(states):
            return_list.append(('NO STATE PROVIDED', nicknames[i]))
    return return_list

# Question 2
def dict_of_states(tuples):
    """
    ##############################################################
    takes a list of nicknames and return a dictionary, each key
    is the state and the values are a list of nicknames
    ##############################################################

    >>> dict_of_states([('AL', 'Cotton State'),
    ... ('LA', 'Pelican State'), ('LA', 'Creole State'),
    ... ('AL', 'Yellowhammer State'), ('LA', 'Sugar State'),
    ... ('MS', 'Magnolia State')])
    {'AL': ['Cotton State', 'Yellowhammer State'], \
'LA': ['Pelican State', 'Creole State', 'Sugar State'], \
'MS': ['Magnolia State']}

    >>> dict_of_states([('MO', 'Show Me State'),
    ... ('NY', 'Empire State'), ('NO STATE PROVIDED', 'Lone Star State')])
    {'MO': ['Show Me State'], 'NY': ['Empire State'], \
'NO STATE PROVIDED': ['Lone Star State']}
    
    >>> dict_of_states([('NO STATE PROVIDED', 'Granite State'), \
    ('NO STATE PROVIDED', 'Sooner State')])
    {'NO STATE PROVIDED': ['Granite State', 'Sooner State']}

    # Add at least 3 doctests below here #
    >>> dict_of_states([])
    {}
    
    >>> dict_of_states([('LA', 'Cotton State'),
    ... ('LA', 'Pelican State'), ('LA', 'Creole State'),
    ... ('LAL', 'Yellowhammer State'), ('LAL', 'Sugar State'),
    ... ('LAL', 'Magnolia State')])
    {'LA': ['Cotton State', 'Pelican State', 'Creole State'], \
'LAL': ['Yellowhammer State', 'Sugar State', 'Magnolia State']}

    >>> dict_of_states([('CA', 'Golden State'), ('LA', 'Pelican State'), 
    ... ('CA', 'Earthquake State')])
    {'CA': ['Golden State', 'Earthquake State'], 'LA': ['Pelican State']}
    """
    return_dict = {}
    for states in tuples:
        state_abbrv = states[0]
        if state_abbrv not in return_dict:
            return_dict[state_abbrv] = [states[1]]
        elif state_abbrv in return_dict:
            nickname_list = return_dict.get(state_abbrv)
            nickname_list.append(states[1])
            return_dict[state_abbrv] = nickname_list
    return return_dict

# Question 3.1
def gambling_in_vegas(profit_history):
    """
    ##############################################################
    Takes in a list of lists and returns a dictionary with keys 
    labeled to the slot machine, values are the money either won 
    or lost at that slot machine
    ##############################################################

    >>> gambling_in_vegas ([[-123, -231, -82], [-340, -158, -225]])
    {'1': -463, '2': -389, '3': -307}
    >>> gambling_in_vegas([[-865, -342, 5]])
    {'1': -865, '2': -342, '3': 5}
    >>> gambling_in_vegas([[-954, -234, -235], \
    [-1040, -350, -394], [-70, -43, -23]])
    {'1': -2064, '2': -627, '3': -652}

    # Add at least 3 doctests below here #
    >>> gambling_in_vegas([[]])
    {'1': 0, '2': 0, '3': 0}
    >>> gambling_in_vegas([[-865, -342, 5], []])
    {'1': -865, '2': -342, '3': 5}
    >>> gambling_in_vegas([[], [-865, -342, 5], []])
    {'1': -865, '2': -342, '3': 5}
    >>> gambling_in_vegas([])
    {'1': 0, '2': 0, '3': 0}
    """
    return_dict = {}
    if len(profit_history) == 0:
        return {'1': 0, '2': 0, '3': 0}
    for lists in profit_history:
        if len(lists) == 0 and len(return_dict) == 0:
            return_dict['1'] = 0
            return_dict['2'] = 0
            return_dict['3'] = 0
        elif len(lists) == 0 and len(return_dict) != 0:
            return_dict = return_dict
        else:
            for i in range(len(lists)):
                slot_machine = str(i + 1)
                if slot_machine not in return_dict:
                    return_dict[slot_machine] = lists[i]
                elif slot_machine in return_dict:
                    profit = return_dict.get(slot_machine) + lists[i]
                    return_dict[slot_machine] = profit
    return return_dict



# Question 3.2
def luck_mechanism(records):
    """
    ##############################################################
    calucalte players luck with the formula provided
    if player gains money from any slot machine, luck is -2
    return dictionary with original dictionary and a key 'luck' 
    added, value is 'You are Lucky' if luck is positive,
    'Fair game' if luck is 0, 'Not this time' if luck is negative
    ##############################################################

    >>> case1 = {'1': -865, '2':-342, '3': 5}
    >>> luck_mechanism(case1)
    {'1': -865, '2': -342, '3': 5, 'luck': 'Not this time'}
    >>> case2 = {'1': -2064, '2': -627, '3': -652}
    >>> luck_mechanism(case2)
    {'1': -2064, '2': -627, '3': -652, 'luck': 'You are Lucky'}
    >>> case3 = {'1': -463, '2': -389, '3': -307}
    >>> luck_mechanism(case3)
    {'1': -463, '2': -389, '3': -307, 'luck': 'You are Lucky'}

    # Add at least 3 doctests below here #
    >>> case4 = {'1': 0, '2': 0, '3': 0}
    >>> luck_mechanism(case4)
    {'1': 0, '2': 0, '3': 0, 'luck': 'Not this time'}
    >>> case5 = {'1': 2000, '2': 0, '3': 0}
    >>> luck_mechanism(case5)
    {'1': 2000, '2': 0, '3': 0, 'luck': 'Not this time'}
    >>> case6 = {'1': -500, '2': -750, '3': 0}
    >>> luck_mechanism(case6)
    {'1': -500, '2': -750, '3': 0, 'luck': 'Fair game'}
    """
    return_dict = records
    history = list(records.values())
    third_in_list = 2
    if history[0] > 0 or history[1] > 0 or history[third_in_list] > 0:
        luck = -2
    else:
        luck = 0.001 * abs(history[0]) + 0.002 * abs(history[1]) + \
        min(0.005 * abs(500 - abs(history[2])), 0.003 * \
        abs(history[third_in_list])) - 2
    if luck > 0:
        return_dict['luck'] = 'You are Lucky'
    elif luck == 0:
        return_dict['luck'] = 'Fair game'
    elif luck < 0:
        return_dict['luck'] = 'Not this time'
    return return_dict

# Question 4
def smaller_collection(collections):
    """
    ##############################################################
    takes in a dictionary and returns a list of unique items in 
    the values of the dictionary
    ##############################################################

    >>> exploration1 = {'team1': ['blue dartwing', 'elves ear'], \
    'team2': ['hawk beak', 'histcarp']}
    >>> out = set(smaller_collection(exploration1))
    >>> set(['blue dartwing', 'elves ear', 'hawk beak', 'histcarp']) == out
    True
    >>> exploration2 = {'team1': ['deathbell', 'deathbell'], 'team2': []}
    >>> smaller_collection(exploration2)
    ['deathbell']
    >>> exploration3 = {'team1': ['deathbell'], \
    'team2': ['blue dartwing', 'histcarp'], 'team3': ['histcarp']}
    >>> out = set(smaller_collection(exploration3))
    >>> out == set(['deathbell', 'blue dartwing', 'histcarp'])
    True

    # Add at least 3 doctests below here #
    >>> exploration4 = {'team1': ['a'], 'team2': ['a'], 'team3': ['a']}
    >>> smaller_collection(exploration4)
    ['a']
    >>> exploration5 = {'team1': [], 'team2': []}
    >>> smaller_collection(exploration5)
    []
    >>> exploration6 = {'team1': ['a'], 'team2': ['a', 'b'], 'team3': \
['a', 'b', 'c']}
    >>> smaller_collection(exploration6)
    ['a', 'b', 'c']
    """
    all_list = []
    for keys in collections:
        all_items = collections.get(keys)
        for items in all_items:
            if items in all_list:
                all_list = all_list
            else:
                all_list.append(items)
    return all_list

# Question 5.1 Part 1
def count_lines_1(filepath):
    """
    ##############################################################
    return number of lines in file using for
    ##############################################################

    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    4

    # Add at least 3 doctests below here #
    >>> count_lines_1('files/test3.txt')
    0
    >>> count_lines_1('files/test4.txt')
    4
    >>> count_lines_1('files/test5.txt')
    3
    """
    with open(filepath) as f:
        count = 0
        for line in f:
            count = count + 1
    return count    


# Question 5.1 Part 2
def count_lines_2(filepath):
    """
    ##############################################################
    return number of lines in file using read()
    ##############################################################

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    4

    # Add at least 3 doctests below here #
    >>> count_lines_1('files/test3.txt')
    0
    >>> count_lines_1('files/test4.txt')
    4
    >>> count_lines_1('files/test5.txt')
    3
    """
    with open(filepath) as f:
        read_data = f.read()
        count = len(read_data.split('\n'))
    return count

# Question 5.1 Part 3
def count_lines_3(filepath):
    """
    ##############################################################
    return number of lines in file using readlines()
    ##############################################################

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    4
    
    # Add at least 3 doctests below here #
    >>> count_lines_1('files/test3.txt')
    0
    >>> count_lines_1('files/test4.txt')
    4
    >>> count_lines_1('files/test5.txt')
    3
    """
    with open(filepath) as f:
        lines = f.readlines()
        count = len(lines)
    return count

# Question 5.2
def items_only(filepath):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> items_only('files/ings1.txt')
    ['rock', 'coins', 'fish']
    >>> items_only('files/ings2.txt')
    ['rock', 'rock', 'fish', 'fish']
    >>> items_only('files/empty_trip.txt')
    []

    # Add at least 3 doctests below here #
    >>> items_only('files/ings3.txt')
    ['c', 'g']
    >>> items_only('files/ings4.txt')
    ['j']
    >>> items_only('files/ings5.txt')
    ['a', 'b', 'c', 'd', 'f']
    """
    first = []
    with open(filepath) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip('\n')
            if len(lines[i]) == 0:
                first = first
            else:
                item_index = 2
                first.append((lines[i].split(','))[item_index])
    return first

# Question 5.3
def case_letters(filepath):
    """
    ##############################################################
    takes filepath and write the number of uppercase and lowercase
    letters in entire filepath in separate lines.
    function returns None.
    ##############################################################

    >>> case_letters('files/AlErNaTiNg.txt')
    >>> with open('files/AlErNaTiNg.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    5
    13
    >>> case_letters('files/another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    19

    # Add at least 3 doctests below here #
    >>> case_letters('files/ANOTHER_TEST.txt')
    >>> with open('files/ANOTHER_TEST.txt', 'r') as outfile3:
    ...    print(outfile3.read().strip())
    11
    8
    >>> case_letters('files/aLeRnAtInG.txt')
    >>> with open('files/aLeRnAtInG.txt', 'r') as outfile4:
    ...    print(outfile4.read().strip())
    5
    13
    >>> case_letters('files/NOTalternatingATall.txt')
    >>> with open('files/NOTalternatingATall.txt', 'r') as outfile5:
    ...    print(outfile5.read().strip())
    5
    22
    """
    with open(filepath, 'w') as f:
        count_upper = 0
        count_lower = 0
        for i in filepath:
            if i.isupper():
                count_upper += 1
            if i.islower():
                count_lower += 1
        f.write(str(count_upper) + '\n')
        f.write(str(count_lower))
    return None

# Question 5.4
def map_age(filepath):
    """
    ##############################################################

    ##############################################################

    >>> map_age('files/age1.txt')
    26
    >>> with open('files/mappings.txt', 'r') as f:
    ...    print(f.readlines()[0].strip())
    adult
    >>> map_age('files/age2.txt')
    17
    >>> with open('files/mappings.txt', 'r') as f:
    ...    print(f.readlines()[-1].strip())
    teenager

    # Add at least 3 doctests below here #
    >>> map_age('files/age3.txt')
    6
    >>> with open('files/mappings.txt', 'r') as f:
    ...    print(f.readlines()[-1].strip())
    kid
    >>> map_age('files/age4.txt')
    -6
    >>> with open('files/mappings.txt', 'r') as f:
    ...    print(f.readlines()[-1].strip())
    not a valid age
    >>> map_age('files/age5.txt')
    27
    >>> with open('files/mappings.txt', 'r') as f:
    ...    print(f.readlines()[-1].strip())
    adult
    """
    with open(filepath) as f:
        lines = f.readlines()
        first_age_limit = 14
        second_age_limit = 15
        third_age_limit = 19
        for i in range(len(lines)):
            lines[i] = int(lines[i].strip('\n'))
        with open('files/mappings.txt', 'a') as m:
            for age in lines: 
                if age < 0:
                    m.write('not a valid age' + '\n')
                elif age <= first_age_limit:
                    m.write('kid' + '\n')
                elif age <= third_age_limit:
                    m.write('teenager' + '\n')
                else: 
                    m.write('adult' + '\n')
    return sum(lines)

# Question 6
def correctness():
    """
    returns a list with three integers.

    >>> lst = correctness()
    >>> type(lst) is list
    True
    >>> len(lst) == 3
    True
    >>> type(sum(lst)) is int
    True

    # NO MORE TESTS ARE NEEDED HERE #
    """
    assert_needed = [2, 2, 4]
    return assert_needed