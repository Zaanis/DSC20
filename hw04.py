"""
DSC 20 HW 04
Name: Joshua Chen   
PID: A16810747
"""

#Question 1
def champion_filter(names, categories):
    """
    Takes 2 lists of strings as inputs, names and categories, name are 
    champions name, category is category of champion, 2 list should have 
    same name, return a list of tuples with champions in the category
    Fighter, Marksman, and Mage

    >>> names1 = ['Aatrox', 'Ashe', 'Anivia', 'Bard']
    >>> categories1 = ['Fighter', 'Marksman', 'Mage', 'Support']
    >>> champion_filter(names1, categories1)
    [('Aatrox', 'Fighter'), ('Ashe', 'Marksman'), ('Anivia', 'Mage')]
    >>> categories2 = []
    >>> champion_filter(names1, categories2)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> names2 = ['Lulu', 'Karma', 'Janna', 'Bard']
    >>> categories3 = ['Support', 'Support', 'Support', 'Support']
    >>> champion_filter(names2, categories3)
    []

    ###Add three more doctests
    >>> names3 = ['Master Yi', 'Kayn', 'Xin Zhao']
    >>> categories4 = ['Fighter', 'Fighter', 'Fighter']
    >>> champion_filter(names3, categories4)
    [('Master Yi', 'Fighter'), ('Kayn', 'Fighter'), ('Xin Zhao', 'Fighter')]
    >>> champion_filter(names1, categories4)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> champion_filter(names1, [1, 2, 3])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert all(isinstance(name, str) for name in names)
    assert all(isinstance(category, str) for category in categories)
    assert len(names) == len(categories)
    assert type(names) == list and type(categories) == list
    return list(filter(lambda x: x != 'N/A', list(map(lambda name, category: \
    (name, category) if category in ['Fighter', 'Marksman', 'Mage'] \
    else 'N/A', names, categories))))


#Question 2
def select_items(combinations):
    """
    function takes a list of dictionaries, in each dictionary, keys are the 
    names of the items, corresponding values are positive numbers.
    Item will enhance champion AP if AP in item name
    Cassiopeia is mage, initial AP of 50, skip shoe items
    return tuple in format: dictionary that brings highest AP, final AP

    >>> example1 = [{'AD_hammer': 200, 'AP_Tear': 20}, {'AP_ring': 30}]
    >>> select_items(example1)
    ({'AP_ring': 30}, 80)
    >>> example2 = [{'AP_shoes': 200, 'AP_Tear': 20}, {'AP_shoes': 30}]
    >>> select_items(example2)
    ({'AP_shoes': 200, 'AP_Tear': 20}, 70)
    >>> example3 = [{}, {}]
    >>> select_items(example3)
    ({}, 50)

    ###Add three more doctests
    >>> example3 = [{'AP_s': 200, 'AP_T': 20, 'A': 0, 'B': 0, 'C': 0, \
        'D': 0, 'E':0}]
    >>> select_items(example3)
    ({}, 50)
    >>> example4 = [{'AP_s': 200, 'AD_T': 20}, {'AP_A': 1000}, {'AP_C': 10000}]
    >>> select_items(example4)
    ({'AP_C': 10000}, 10050)
    >>> example5 = [{'AD_hammer': 20000, 'AP_Tear': 2}, {'AP_r': 3}]
    >>> select_items(example5)
    ({'AP_r': 3}, 53)
    """
    base = 50
    combinations = list(map(lambda x: x if len(x) <= 6 else {}, combinations))
    sorting = lambda items: (base + sum(list(map(lambda AP: items.get(AP), \
    list(filter(lambda name: name if 'AP' in name and 'shoe' \
    not in name else False, items))))), items)
    reversed = max(list(map(sorting, combinations)))
    return (reversed[1], reversed[0])


#Question 3
def calculate_experience(scores):
    """
    calculate XP
    kills worth 100 each, every 5 kills count as ultra kill, add 250
    deaths subtract 25
    assists add 30 each if kill>assist, 50 if kill<assist, 40 if kill=assist
    gold worth gold*0.1 rounded to closest integer
    if negative xp calcualted, return 0
    return the total xp
    
    >>> example1 = [[17, 1, 3, 3400], [9, 5, 4, 2731], [1, 2, 14, 2315]]
    >>> calculate_experience(example1)
    [2855, 1418, 982]
    >>> example2 = [[0, 0, 0, 0], [0, 17, 0, 100], [1, 1, 1, 0]]
    >>> calculate_experience(example2)
    [0, 0, 115]
   
    ###Add three more doctests
    >>> example3 = [[0, 0, 0, 10000], [0, 0, 0, 100], [100, 0, 0, 0]]
    >>> calculate_experience(example3)
    [1000, 10, 15000]
    >>> example4 = [[0, 0, 0]]
    >>> calculate_experience(example4)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> example5 = [10000]
    >>> calculate_experience(example5)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert type(scores) == list
    assert all(isinstance(x, list) for x in scores)
    assert all(isinstance(j, int) for x in scores for j in x)
    assert all(len(x) == 4 for x in scores)
    k1, k2, k3 = 100, 250, 5
    d1 = -25
    a1, a2, a3 = 30, 50, 40
    g1 = 0.1
    k, d, a, g = 0, 1, 2, 3
    kill = lambda kills: kills * k1 + (kills // k3) * k2
    death = lambda deaths: deaths * d1
    assist = lambda assists, kills: a1 * assists if kills > assists \
    else a2 * assists if kills < assists else a3 * assists    
    gold = lambda golds: round(golds * g1)
    orig_xp = list(map(lambda z: kill(z[k]) + death(z[d]) + \
    assist(z[a], z[k]) + gold(z[g]), scores))
    return list(map(lambda w: w if w >= 0 else 0, orig_xp))

#Question 4
def calculate_level(scores, level):
    """
    take lists of scores and players current level and calculate level they 
    should be promoted to after given matches
    lowest level is 1, 1 to 2 need 2000xp, then number of points for subsequent
    level increases by 200
    return the final level

    >>> example1 = [[17, 1, 3, 3400], [9, 5, 4, 2731], [1, 2, 14, 2315]]
    >>> calculate_level(example1, 1)
    3
    >>> calculate_level(example1, 10)
    11
    >>> calculate_level([], 1)
    1

    ###Add three more doctests
    >>> calculate_level(example1, 100)
    100
    >>> example2 = [[170, 1, 3, 34000], [90, 5, 4, 27310], [10, 2, 14, 23150]]
    >>> calculate_level(example2, 100)
    102
    >>> calculate_level(example2, 1)
    15
    >>> calculate_level(example2, 1000)
    1000
    """
    xp = sum(calculate_experience(scores))
    base = 2000
    level_up = 200
    threshold = base + level_up * (level - 1)
    return_level = level
    while xp > threshold:
        return_level += 1
        threshold += level_up
        xp -= threshold
    return return_level