"""
DSC 20 Lab 04
Name: Joshua Chen
PID: A16810747
"""

#Question 1
def order_66(squads):
    """
    >>> order_66([["clone", "clone", "clone", "jedi"], ["clone", "jedi"]])
    ['executed', 'survived']
    >>> order_66([["clone", "clone", "clone", "clone", "jedi", "jedi"], \
["clone", "jedi", "clone"], ["jedi", "jedi", "clone"]])
    ['survived', 'survived', 'survived']
    >>> order_66([])
    []
    """
    return list(map(lambda x: 'executed' if 2 * x.count('jedi') <\
    x.count('clone') else 'survived', squads))



#Question 2
def midichlorian(people, threshold):
    """
    >>> midichlorian([("Anakin Skywalker", 27000), ("Moff Tarkin", 2500), \
("Din Djarin", 6000), ("Yoda", 19000), ("Obi-Wan Kenobi", 13000), \
("Luke Skywalker", 25000), ("Jar Jar Binks", 1000)], 6000)
    ['Anakin Skywalker', 'Yoda', 'Obi-Wan Kenobi', 'Luke Skywalker']
    >>> midichlorian([("General Grievous", 0), ("Jango Fett", 4500)], 5000)
    []
    """
    return list(map(lambda x: x[0], \
    list(filter(lambda x: x[1]>threshold, people))))

#Question 3
def podracer(bets):
    """  
    >>> bets_1 = {"Windu": [100, 20, 10], \
"Quigon": [400, 0, 50], \
"Obiwan": [0, 200, 150], \
"Jabba": [600, 100, 500]}
    >>> podracer(bets_1)
    ['Windu', 'Quigon']
    >>> bets_2 = {"Boba Fett": [400, 300, 300], \
"Yoda": [300, 1000, 10]}
    >>> podracer(bets_2)
    []
    >>> bets_3 = {"Han Solo": [10, 5, 4], \
"Chewbacca": [250, 30, 210], \
"C3PO": [700, 40, 3]}
    >>> podracer(bets_3)
    ['Han Solo', 'Chewbacca', 'C3PO']
    """
    return list(filter(lambda x: x != 'NAN', list(map(lambda name, profit: \
    name if profit[0] - profit[1] - profit[2] > 0 else 'NAN', \
    list(bets.keys()), list(bets.values()))))) 

#Question 4
def darth(names):
    """
    >>> darth(["sidious", "Maul", "Yoda", "Vader", "Obi-Wan Kenobi", \
"Luke", "plagueis"])
    ['Darth Sidious', 'Darth Maul', 'Darth Vader', 'Darth Plagueis']
    >>> darth([])
    []
    >>> darth(['tyRanus', 'CaldotH', 'b', 'a', 'grogu', 'Ahsoka Tano', \
'bob builDer'])
    ['Darth Tyranus', 'Darth Caldoth', 'Darth B', 'Darth Bob Builder']
    """
    return list(map(lambda x: ('Darth ' + x).title(), \
    list(filter(lambda name: name[0] and name[-1] \
    not in ['a', 'e', 'i', 'o', 'u'], names))))

#Question 5
def sand(places):
    """
    >>> sand({"Tatooine": ["sand", "coarse", "rough", "irritating", "hot"], \
"Naboo": ["peaceful", "swampy", "green"], \
"Mustafar": ["rough", "fire", "irritating"], \
"Alderaan": ["beautiful", "no sand"]})
    2
    >>> sand({"Coruscant": []})
    1
    >>> sand({"Hoth": ["cold"], "Kamino": ["stormy", "inhospitable"], \
"Endor": ["foresty", "grassy"], "Vanqor": ["very irritating", "rocky"]})
    4
    >>> sand({"Geonosis": ["coarse sand"]})
    1
    """
    nothing = lambda x,y: False if set(x) & set(y) else True
    return len(list(filter(lambda x: x != 'NAN', list(map(lambda name, \
    description: name if nothing(description, \
    ['sand', 'coarse', 'rough', 'irritating']) else 'NAN', \
    list(places.keys()), list(places.values()))))))


#Question 6
def death_star(coordinates, death_star):
    """
    >>> death_star({"Coruscant": (0, 0, 0), \
"Batuu": (-401.72, -561.84, 4.32)}, (0.5, -0.5, 0))
    ['Coruscant']
    >>> death_star({"Coruscant": (0, 0, 0), \
"Alderaan": (-340.2, -80.01, 0.88)}, (-340.11, -79.72, 1.06))
    ['Alderaan']
    >>> death_star({"Mandalore": (0, -0.5, -0.8)}, (-0.3, -0.5, -0.7))
    ['Mandalore']
    """
    return list(filter(lambda x: x != 'NAN', list(map(lambda name, location: \
    name if all([location[0] - death_star[0] <= 0.5, location[1] - death_star \
    [1] <=0.5, location[2] - death_star[2] <=0.5]) else 'NAN', \
    list(coordinates.keys()), list(coordinates.values())))))
