"""
DSC 20 Homework 01
Name: Joshua Chen
PID: A16810747
"""

# Problem 1

def name_scramble(fname, lname):
    """
    ##############################################################
    reverse fname, take every other character from index 0,
    then take every third character from lname starting index 0,
    return the characters put together as a string
    ##############################################################
    >>> name_scramble("Marina", "Langlois")
    'aiaLgi'
    >>> name_scramble("", "")
    ''
    >>> name_scramble("Sheldon", "Cooper")
    'ndeSCp'
    
    # Add at least 3 doctests below here #
    >>> name_scramble("Sheldon","")
    'ndeS'
    >>> name_scramble("Joshua","C")
    'ahoC'
    >>> name_scramble("J","Chen")
    'JCn'
    """
    fname_reverse = fname[::-1]
    scrambled_name = ""
    x = 0
    while x < len(fname_reverse):
        scrambled_name = scrambled_name + fname_reverse[x]
        x = x + 2
    y = 0
    while y < len(lname):
        scrambled_name = scrambled_name + lname[y]
        y = y + 3
    return scrambled_name


# Problem 2

def close_to_25(age1, age2):
    """
    ##############################################################
    if both age less than 25, return the largest 
    if one age less than 25, one over, return the age less than 25
    if both over or equal 25, return "we are good to go!"
    ##############################################################
    >>> close_to_25(19, 21)
    21
    >>> close_to_25(26, 21)
    21
    >>> close_to_25(26, 27)
    'we are good to go!'
    >>> close_to_25(19, 19)
    19
    
    # Add at least 3 doctests below here #
    >>> close_to_25(1,5)
    5
    >>> close_to_25(100,200)
    'we are good to go!'
    >>> close_to_25(25,24)
    25
    """
    # YOUR CODE GOES HERE #
    if age1 <= 25 and age2 <= 25:
        return max(age1, age2)
    elif age1 > 25 and age2 < 25:
        return age2
    elif age1 < 25 and age2 > 25:
        return age1
    else:
        return 'we are good to go!'    


# Problem 3

def main_driver(name1, name2, name3):
    """
    ##############################################################
    returns the name with largest length
    if there is a tie, return the name that appears last
    ##############################################################
    >>> main_driver("K", "BB", "Joy")
    'Joy'
    >>> main_driver("Joy", "K", "BB")
    'Joy'
    >>> main_driver("BB", "Joy", "K")
    'Joy'
    >>> main_driver("BB", "K", "Jo")
    'Jo'
    >>> main_driver("BB", "Jo", "Su")
    'Su'
    
    # Add at least 3 doctests below here #
    >>> main_driver("A","AB","ABC")
    'ABC'
    >>> main_driver("Paul","John","Josh")
    'Josh'
    >>> main_driver("A","Paul","Rahul")
    'Rahul'
    >>> main_driver("Paul","Joe","Bob")
    'Paul'
    """
    # YOUR CODE GOES HERE #
    return_name = ""
    list_of_name = [name1, name2, name3]
    for names in list_of_name:
        if len(names) >= len(return_name):
            return_name = names
        else:
            return_name = return_name
    return return_name


# Problem 4
# Problem 4.1

def helper_distance(lst, x2, y2):
    """
    ##############################################################
    calculate and return the Euclidean distance between 2 points
    ##############################################################
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance([100, 100], 100.5, 100)
    0.5
    
    # Add at least 3 doctests below here #
    >>> helper_distance([0,0], 5, 12)
    13.0
    >>> helper_distance([1,2], 4, 6)
    5.0
    >>> helper_distance([-5,-12], 5, 12)
    26.0
    """
    # YOUR CODE GOES HERE #

    return ((x2 - lst[0]) ** (2) + (y2 - lst[1]) ** (2)) ** (1/2)


# Problem 4.2:

def all_distances(coordinates, x_coord, y_coord, threshold):
    """
    ##############################################################
    return a list of lists where distance between each place and a
    starting point is less than or equal to the given threshold
    ##############################################################
    >>> all_distances([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> all_distances([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> all_distances ([[100, 100]], 100.5, 100, 0.2)
    []
    
    # Add at least 3 doctests below here #
    >>> all_distances([[0, 1], [0, 0.5], [0, 2]], 0, 0, 1)
    [[0, 1], [0, 0.5]]
    >>> all_distances([[0, 0], [1, 1], [2, 2], [3, 3]] , 4, 0, 0)
    []
    >>> all_distances([[1, 1], [2, 2], [3, 3], [4, 4]], 0, 0, 100)
    [[1, 1], [2, 2], [3, 3], [4, 4]]
    """
    # YOUR CODE GOES HERE #
    drivable = []
    for places in coordinates:
        distance = helper_distance(places, x_coord, y_coord)
        if distance <= threshold:
            drivable.append(places)
        else:
            drivable = drivable
    return drivable


# Problem 5

def places_names(coordinates, x_coord, y_coord, threshold, names):
    """
    ##############################################################
    return the names of the places we can drive to within a 
    threshold
    ##############################################################
    >>> places_names([[0, 0], [30, 20]], 3, 4, 6, \
    ['place1', 'place2'])
    ['place1']
    >>> places_names([[-3, -4], [6, 7]], 3, 4, 10, \
    ['place1', 'place2'])
    ['place1', 'place2']
    >>> places_names ([[100, 100]], 100.5, 100, 0.2, ['place1'])
    []
    
    # Add at least 3 doctests below here #
    >>> places_names([[0, 1], [0, 0.5], [0, 2]], 0, 0, 1, \
    ["my house", "your house", "his house"])
    ['my house', 'your house']
    >>> places_names([[0, 0], [1, 1], [2, 2], [3, 3]] , 4, 0, \
    0, ['place1', 'place2', 'place3', 'place4'])
    []
    >>> places_names([[1, 1], [2, 2], [3, 3], [4, 4]], 0, 0, \
    100, ['place1', 'place2', 'place3', 'place4'])
    ['place1', 'place2', 'place3', 'place4']
    """
    # YOUR CODE GOES HERE #
    available_places = all_distances(coordinates, x_coord, y_coord, threshold) 
    name_of_places = []
    for coords in available_places:
        name_of_places.append(names[coordinates.index(coords)])
    return name_of_places


#Problem 6

def message(i_name, dow, time, c_name):
    """
    ##############################################################
    returns an invitation as a string, including name of invitee,
    day of week, time of day, name of captain in the format:
    Dear <name>,
    Please join our meeting on <day of the week> at <time>.

    Team captain: <captain name>
    ##############################################################
    >>> print(message("Freya", "Friday", "4:00 PM", "Marina"))
    Dear Freya,
    Please join our meeting on Friday at 4:00 PM.
    <BLANKLINE>
    Team captain: Marina
    >>> print(message("Penny", "Monday", "", "Sheldon"))
    Dear Penny,
    Please join our meeting on Monday at .
    <BLANKLINE>
    Team captain: Sheldon
    
    # Add at least 3 doctests below here #
    >>> print(message("","","",""))
    Dear ,
    Please join our meeting on  at .
    <BLANKLINE>
    Team captain: 
    >>> print(message("Joe","Sunday","12:00AM","Bob"))
    Dear Joe,
    Please join our meeting on Sunday at 12:00AM.
    <BLANKLINE>
    Team captain: Bob
    >>> print(message("A","B","C","D"))
    Dear A,
    Please join our meeting on B at C.
    <BLANKLINE>
    Team captain: D
    """
    # YOUR CODE GOES HERE #
    invitation = "Dear " + i_name + ",\n" + "Please join our meeting on " \
    + dow + " at " + time + ".\n\nTeam captain: " + c_name
    return invitation

# Problem 7

def seat_number(lst):
    """
    ##############################################################
    Takes a list of members and return another list, where element
    is length of string from given list. If there are strings of
    equal length, assign "taken" instead
    ##############################################################
    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]
    
    # Add at least 3 doctests below here #
    >>> seat_number(["Joe", "Bob"])
    [3, 'taken']
    >>> seat_number(["A", "AB", "ABC", "ABCD"])
    [1, 2, 3, 4]
    >>> seat_number(["A", "AB", "C", "ABC", "BA", "AAA", "ABCD"])
    [1, 2, 'taken', 3, 'taken', 'taken', 4]
    """
    # YOUR CODE GOES HERE #
    seat_number = []
    for names in lst:
        if len(names) in seat_number:
            seat_number.append("taken")
        else:
            seat_number.append(len(names))
    return seat_number


# Problem 8

def suv_vs_minivan(names):
    """
    ##############################################################
    return True is 'SUV' occurs more than 'Minivan'
    return False otherwise
    list could contain items that does is not 'SUV' or 'Minivan'
    ##############################################################
    >>> suv_vs_minivan(["SUV", "Minivan", "SUV"])
    True
    >>> suv_vs_minivan(["Minivan", "Minivan"])
    False
    >>> suv_vs_minivan(["SUV", "compact", "mid-size", "Minivan"])
    False
    
    # Add at least 3 doctests below here #
    >>> suv_vs_minivan(["SUV", "minivan"])
    True
    >>> suv_vs_minivan(["SUV", "SUV", "Minivan", "Minivan", "Toyota", "SUV"])
    True
    >>> suv_vs_minivan([""])
    False
    """
    # YOUR CODE GOES HERE #
    suv_counter = names.count('SUV')
    minivan_counter = names.count('Minivan')
    if suv_counter > minivan_counter:
        return True
    else:
        return False
    


# Problem 9

def age_average(lst):
    """
    ##############################################################
    returns the average age rounded to 1 decimal place
    return "0.0" if list is empty
    ##############################################################
    >>> age_average(["1", "2", "3"])
    '2.0'
    >>> age_average(["111", "205", "377"])
    '231.0'
    >>> age_average(["777", "-999"])
    '-111.0'
    >>> age_average([])
    '0.0'
    
    # Add at least 3 doctests below here #
    >>> age_average(["0", "1", "2", "3"])
    '1.5'
    >>> age_average(["-1", "-2", "-3"])
    '-2.0'
    >>> age_average(["-1", "1", "-2", "2"])
    '0.0'
    """
    # YOUR CODE GOES HERE #
    if len(lst) == 0:
        return '0.0'
    else:
        total_age = 0
        for age in lst:
            total_age = total_age + int(age)
        average = round(total_age/len(lst), 1)
    return str(average)


# Problem 10

def split_teams(lst, captain):
    """
    ##############################################################
    returns 2 team lists as a tuple
    first team have even index from the list
    second team have odd index from the list
    first team's list has captain name as first element
    second team's list has captain name as last element
    ##############################################################
    >>> split_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> split_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> split_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])
    
    # Add at least 3 doctests below here #
    >>> split_teams(["p1"], "Joe")
    (['Joe', 'p1'], ['Joe'])
    >>> split_teams(["p1", "p2"], "BOB")
    (['BOB', 'p1'], ['p2', 'BOB'])
    >>> split_teams(["p1", "p2", "p3", "p4", "p5", "p6", "p7"], "Marina")
    (['Marina', 'p1', 'p3', 'p5', 'p7'], ['p2', 'p4', 'p6', 'Marina'])

    """
    
    # YOUR CODE GOES HERE #
    first_list = [captain]
    second_list = []
    i = 0
    while i < len(lst):
        first_list.append(lst[i])
        i = i + 2
    j = 1
    while j < len(lst):
        second_list.append(lst[j])
        j = j + 2
    second_list.append(captain)
    list_as_tuple = first_list, second_list
    return list_as_tuple

