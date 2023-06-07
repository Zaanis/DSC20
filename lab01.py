"""
DSC 20 Lab 01
Name: Joshua Chen
PID: A16810747
"""

# Problem 1
def driver_age(lst):
    """
    Checks whether at least one driver is 25 or older in a given list
    ---
    Parameters:
    lst: a list of positive integers, might be empty
    ---
    Returns True if at least one driver is 25 or older,
    False otherwise

    >>> driver_age([19, 22, 21])
    False
    >>> driver_age([19, 23, 15, 27])
    True
    >>> driver_age([])
    False
    """
    if len(lst) > 0:
        for i in range(len(lst)):
            if lst[i] > 25:
                x = True
            else:
                x = False
    else: 
        x = False
    return x
# # Problem 2
def over_25_counter_variable(lst):
    """
    Counts how many ages are 25 or older in a given list.
    ---
    Parameters:
    lst: a list of positive integers, might be empty
    ---
    Returns the number of drivers whose age is 25 or older.

    >>> over_25_counter_variable([])
    0
    >>> over_25_counter_variable([12, 15])
    0
    >>> over_25_counter_variable([12, 25, 30])
    2
    >>> over_25_counter_variable([30, 15, 24])
    1
    """
    x = 0
    for i in range(len(lst)):
        if lst[i] >= 25:
            x += 1
    return x
#
#
# Problem 3
def team_captain(first_name, last_name):
    """
    Concatenates the string parameters into the output string.
    ---
    Parameters:
    first_name: first name, as a string
    last_name: last name, as a string
    ---
    Returns a string who is a team's captain

    >>> team_captain("Marina", "Langlois")
    'Team captain is Marina Langlois'
    >>> team_captain("Marina", "")
    'Team captain is Marina '
    >>> team_captain("the", "best")
    'Team captain is the best'
    """
    name = "Team captain is " + first_name + " " + last_name
    return name
#
#
# Problem 4
def team_name(names):
    """
    Creates the name for the team by putting together first and last
    characters of each name. Adds a space if the input only has one
    character.

    ---
    Parameters:
    names: list of names, as strings
    ---
    Returns a team name, as a string

    >>> names = ["Marina", "J", "Mike"]
    >>> team_name(names)
    'MaJ Me'
    >>> names = ["Sheldon", "Leonard", "Raj", "Howard"]
    >>> team_name(names)
    'SnLdRjHd'
    >>> names = ["Y", "J", "B"]
    >>> team_name(names)
    'Y J B '
    """
    team = ""
    for i in range(len(names)):
        if len(names[i]) == 1:
            team = team + names[i] + " "
        else:
            team = team + (names[i][0] + names[i][-1])
    return team
#
#
# # Problem 5.1
def team_slogan_concat(words, separator):
    """
    Creates a slogan from the words, adding a separator between them.
    ---
    Parameters:
    words: list of words, as strings
    separator: single character
    ---
    Returns a string

    >>> words = ["Let", "it", "be", "fun"]
    >>> team_slogan_concat(words, " ")
    'Let it be fun'
    >>> words = ["Stay", "focused", "stay", "cool"]
    >>> team_slogan_concat(words, "-")
    'Stay-focused-stay-cool'
    """
    slogan = ""
    for i in range(len(words)-1):
        slogan = slogan + words[i] + separator
    return slogan + words[len(words)-1]


# # Problem 5.2
def team_slogan_join(words, separator):
    """
    Creates a slogan from the words, adding a separator between them.
    ---
    Parameters:
    words: list of words, as strings
    separator: single character
    ---
    Returns a string

    >>> words = ["Let", "it", "be", "fun"]
    >>> team_slogan_join(words, " ")
    'Let it be fun'
    >>> words = ["Stay", "focused", "stay", "cool"]
    >>> team_slogan_join(words, "-")
    'Stay-focused-stay-cool'
    """
    return separator.join(words)
#
#
# # Problem 6.1
def drawing(symbol, repeat):
    """
    Creates a string of symbols
    ---
    Parameters:
    symbol: a single character
    repeat: positive integer
    ---
    Returns a string of symbols repeated a given number of times.

    >>> drawing("-", 4)
    '----'
    >>> drawing("+", 5)
    '+++++'
    """
    return symbol*repeat
#
#
# # Problem 6.2
def drawing_longer(symbols, repeats):
    """
    Creates a string of symbols
    ---
    Parameters:
    symbols: a list of single characters
    repeat: a list of positive integers, has the same length
    as symbols
    ---
    Returns a string of symbols repeated a corresponding number of
    times.

    >>> drawing_longer(['-', '+'], [4, 5])
    '----+++++'
    """
    draw = ""
    for i in range(len(symbols)):
        draw = draw + symbols[i]*repeats[i]
    return draw
#
#
# # Problem 7.1
def hotel_rating_average(ratings):
    """
    Finds average where numbers lower than 5 get a value of a 0
    ---
    Parameters:
    ratings: list of integers ranging from 1 to 10
    ---
    Returns an average rounded to the second decimal place

    >>> hotel_rating_average([10, 10, 10])
    10.0
    >>> hotel_rating_average([10, 10, 1])
    6.67
    >>> hotel_rating_average([3, 2, 1])
    0.0
    """
    rate = 0
    for i in range(len(ratings)):
        if ratings[i]< 5:
            ratings[i] = 0
    for i in range(len(ratings)):
        rate =  rate + ratings[i]
    return round(rate/len(ratings),2)
#
#
# Problem 7.2
def hotel_rating_best_average(ratings, names):
    """
    Finds the best route name based on the hotel averages
    ---
    Parameters:
    ratings: list of lists, where each list contains integers
    ranging from 1 to 10
    names: list of lists, where each list contains route names.
    ---
    Returns the best route name based on the hotel averages
    as a string

    >>> ratings = [[1, 10, 5], [4, 6, 9]]
    >>> names = ["op1", "op2"]
    >>> hotel_rating_best_average(ratings, names)
    'op1'

    >>> ratings = [[6, 10, 5], [10, 10, 9], [6, 6, 7]]
    >>> names = ["op1", "op2", "op3"]
    >>> hotel_rating_best_average(ratings, names)
    'op2'

     >>> hotel_rating_best_average([], [])
     'No route to choose from'
    """
    newrating = []
    hotel = ""
    if len(ratings) == 0:
        hotel = "No route to choose from"
    else:
        for i in range(len(ratings)):
            newrating.append(hotel_rating_average(ratings[i]))
        maximum = max(newrating)
        hotel = names[newrating.index(maximum)]
    return hotel



# # Problem 8
def password(text, number, boolean):
    """
    Creates a password based on the given parameters:
    text is reversed, numbers becomes either even or odd, boolean
    value is flipped
    ---
    Parameters:
    text: a string
    number: an integer
    boolean: a boolean value
    ---
    Returns a password by adding altered components to string.

    >>> password("trip", "is", True)
    'ERROR!'
    >>> password(17, "is", True)
    'ERROR!'
    >>> password("trip", 18, 20)
    'ERROR!'
    >>> password("trip", 18, False)
    'pirt19True'
    >>> password("car", 21, True)
    'rac20False'
    """
    message = ""
    if type(text) != str:
        message = "ERROR!"
    elif type(number) != int:
        message = "ERROR!"
    elif type(boolean) != bool:
        message = "ERROR!"
    else:
        if number%2 == 0:
            number = number + 1
            message = text[::-1] + str(number) + str(not boolean)
        else:
            number = number - 1
            message = text[::-1] + str(number) + str(not boolean)
    return message
