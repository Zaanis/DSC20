"""
DSC 20 Lab 02
Name: Joshua Chen   
PID: A16810747
"""

# Problem 1
def parks(park_names):
    """
    >>> park_names = ["Cardiff", "China Camp", "Delta Meadows"]
    >>> parks(park_names)
    ['ardif', 'hina Cam', 'elta Meadow']
    >>> park_names = ["Estero Bluffs ", 'Garrapata']
    >>> parks(park_names)
    ['stero Bluffs', 'arrapat']
    >>> park_names = ['', 'ML']
    >>> parks(park_names)
    ['will skip', 'will skip']
    """
    park_list = []
    for names in park_names:
        if len(names) < 3:
            park_list.append('will skip')
        else:
            park_list.append(names[1:len(names)-1])

    return park_list


# Problem 2
def many_parks(many_places, threshold):
    """
    >>> many_places = [["Cardiff", "China Camp", "Delta Meadows"], \
    ['Estero Bluffs ', 'Garrapata']]
    >>> many_parks(many_places, 1)
    [['ardif', 'hina Cam', 'elta Meadow'], ['stero Bluffs', 'arrapat']]
    >>> many_parks(many_places, 4)
    [['will skip', 'a ', 'a Mea'], ['ro Blu', 'a']]
    >>> many_places = [["Cardiff", "China Camp", "Delta Meadows"], \
['Estero Bluffs ', 'Garrapata'], ['', 'ML']]
    >>> many_parks(many_places, 5)
    [['will skip', '', ' Me'], ['o Bl', 'will skip'], \
['will skip', 'will skip']]
    """
    return_list = []
    for many_places_list in many_places:
        park_list = []
        for names in many_places_list:                
            if len(names) < threshold * 2:
                park_list.append('will skip')
            else:
                park_list.append(names[threshold:len(names)-threshold])
        return_list.append(park_list)
    return return_list


# Problem 3
def correct_state(places):
    """
    >>> places = [["Cardiff", "CA"], ["China Camp", "CA"], ["Boettler", "OH"]]
    >>> correct_state(places)
    ['CARDIFF', 'CHINA CAMP']
    >>> places = [["Cardiff", "CA"], ["Valley of Fire", "NV"], \
    ["Delta Meadows", "CA"]]
    >>> correct_state(places)
    ['CARDIFF']
    >>> places = [["Boettler", "OH"], ["Cardiff", "CA"], ["China Camp", "CA"]]
    >>> correct_state(places)
    []
    """
    i = 0
    capitalized = []
    while i < len(places):
        if places[i][1] =='CA':
            capitalized.append(places[i][0].upper())
            i = i + 1
        else:
            break
    return capitalized


# Problem 4
def names(input_string, end):
    """
    >>> input_string = "Marina Langlois Anna Freya Sue Pooja"
    >>> names(input_string, 'a')
    4
    >>> input_string = "Marina Langlois Ann!a Freya Sue Pooja"
    >>> names(input_string, 'a')
    3
    >>> input_string = "Marina Langlois An@ns !reys Sue Pooja"
    >>> names(input_string, 's')
    3
    >>> input_string = "Marin! Langloi! Ann!! !rey! Sue Pooja"
    >>> names(input_string, '!')
    3
    """
    all_names = input_string.split(" ")
    count = 0
    for names in all_names:
        if names[-1] == end:
            if names[-2].isalpha():
                count = count + 1
            else:
                count = count
        else:
            count = count
        
    return count


# Problem 5.1
def pr5_1(teams):
    """
    >>> test1 = {"Marina": ["Yacun","Ella"], "Sheldon": ["Penny","Raj"]}
    >>> pr5_1(test1)
    2
    >>> test2 = {}
    >>> pr5_1(test2)
    0
    >>> test3 = {"Marina": [], "Sheldon": [], "Dylan": ["Leo"]}
    >>> pr5_1(test3)
    3
    """
    count = 0
    for keys in teams:
        count = count + 1
    return count


# Problem 5.2
def pr5_2(teams):
    """
    >>> test1 = {"Marina": ["Yacun","Ella"], "Sheldon":["Penny","Raj"]}
    >>> pr5_2(test1)
    ['Marina', 'Sheldon']
    >>> test2 = {}
    >>> pr5_2(test2)
    []
    >>> test3 = {"Marina": [], "Sheldon": [], "Dylan": ["Leo"]}
    >>> pr5_2(test3)
    ['Marina', 'Sheldon', 'Dylan']
    """
    list = []
    for key in teams.keys():
        list.append(key)
    return list


# Problem 5.3
def pr5_3(teams):
    """
    >>> test1 = {"Marina": ["Yacun","Ella"], "Sheldon":["Penny","Raj"]}
    >>> pr5_3(test1)
    2
    >>> test2 = {}
    >>> pr5_3(test2)
    0
    >>> test3 = {"Marina": [], "Sheldon": [], "Dylan": ["Leo"]}
    >>> pr5_3(test3)
    1
    """
    lists = teams.values()
    largest = 0
    for captain in lists:
        count = 0 
        for members in captain:
            count = count + 1
            if count > largest:
                largest = count
            else:
                largest = largest
    return largest


# Problem 5.4
def pr5_4(teams, driver):
    """
    >>> test1 = {}
    >>> pr5_4(test1, 'Marina')
    {'Marina': []}
    >>> test2 = {'Dylan': ['Marina', 'Sheldon']}
    >>> pr5_4(test2, 'Dylan')
    {'Dylan': ['Marina', 'Sheldon']}
    >>> pr5_4(test2, 'Penny')
    {'Dylan': ['Marina', 'Sheldon'], 'Penny': []}
    """
    if driver in teams:
        teams = teams
    else:
        teams.update({driver: []})
    return teams


# Problem 5.5
def pr5_5(teams, driver, team_member):
    """
    >>> test1 = {}
    >>> pr5_5(test1, 'Marina', 'Sheldon')
    {'Marina': ['Sheldon']}
    >>> test2 = {'Dylan': ['Marina', 'Sheldon']}
    >>> pr5_5(test2, 'Dylan', 'Penny')
    {'Dylan': ['Marina', 'Sheldon', 'Penny']}
    >>> test3 = {'Dylan': ['Marina', 'Sheldon']}
    >>> pr5_5(test3, 'Dylan', 'Marina')
    {'Dylan': ['Marina', 'Sheldon', 'Marina']}
    """
    if driver in teams:
        member_list = teams.get(driver)
        member_list.append(team_member)
        teams.update({driver: member_list})
    else:
        teams.update(({driver: [team_member]}))
    return teams


# Problem 5.6
def pr5_6(teams, team_member):
    """
    >>> test1 = {'Dylan': ['Marina', 'Sheldon'], 'Penny': ['Sheldon']}
    >>> pr5_6(test1, 'Sheldon')
    {'Dylan': ['Marina'], 'Penny': []}
    >>> test2 = {'Dylan': []}
    >>> pr5_6(test2, 'haha')
    {'Dylan': []}
    >>> test3 = {'Dylan': ['Marina', 'Sheldon'], 'Penny': []}
    >>> pr5_6(test3, 'Sheldon')
    {'Dylan': ['Marina'], 'Penny': []}
    """
    for driver in teams:
        member_list = teams.get(driver)
        if team_member in member_list:
            member_list.remove(team_member)
        teams.update({driver: member_list})
    return teams


# Problem 6
def secret_language(pass_dict):
    """
    >>> dict1 = {'Dylan': 'haha', 'Marina': 2, 'Penny': 0, 'Sheldon': -1}
    >>> secret_language(dict1)
    'nalyD***********n'
    >>> dict2 = {'': 2, '': 'yeh'}
    >>> secret_language(dict2)
    ''
    >>> dict3 = {'Dy': 5, 'JL': 'ab'}
    >>> secret_language(dict3)
    '**LJ'
    """
    message = ""
    for members in pass_dict:
        if type(pass_dict.get(members)) == str:
            if len(pass_dict.get(members)) % 2 == 0:
                message = message + members[::-1]
        elif type(pass_dict.get(members)) == int:
            if pass_dict.get(members) >= 0:
                message = message + "*" * len(members)
            elif pass_dict.get(members) < 0:
                message = message + members[-1]
             
    return message
