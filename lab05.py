"""
DSC 20 Lab 05
Name: Joshua Chen
PID: A16810747
"""

def identity(x):
    return x

def squared(x):
    return x**2



# Problem 1
def dct_op(dct, func):
    """
    >>> dct = {'Curry': [26,21,30], 'James': [26,22,18]}
    >>> dct_op(dct, squared)
    {'Curry': [676, 441, 900], 'James': [676, 484, 324]}
    >>> dct = {'Poole': [15,11,27,23], 'Tatum': [35,21,22,28], \
'Harden': [28,11,22,19]}
    >>> dct_op(dct, identity)
    {'Poole': [15, 11, 27, 23], 'Tatum': [35, 21, 22, 28], \
'Harden': [28, 11, 22, 19]}
    >>> dct_op(dct, lambda x:x+1)
    {'Poole': [16, 12, 28, 24], 'Tatum': [36, 22, 23, 29], \
'Harden': [29, 12, 23, 20]}
    """
    return {key: [func(x) for x in value] for (key, value) in \
    list(dct.items())}



# Problem 2
def dct_special(dct, func, players):
    """
    >>> dct = {'Curry': [38,21,30], 'James': [26,29,28], 'Tatum': [35,21,22]}
    >>> players = ['Curry', 'Tatum']
    >>> dct_special(dct, identity, players)
    [[38, 21, 30], [35, 21, 22]]
    >>> dct = {'Curry': [38,21,30], 'Tatum': [35,21,22]}
    >>> players = []
    >>> dct_special(dct, squared, players)
    []
    >>> dct = {'Poole': [41,31,21], 'James': [19,29,28], 'Durant': [23,11,32]}
    >>> players = ['James', 'Poole']
    >>> dct_special(dct, squared, players)
    [[1681, 961, 441], [361, 841, 784]]
    """
    return [[func(x) for x in dct.get(y)] for y in dct.keys() if y in players]



# Problem 3
def nba_stats(dct, func, stats):
    """
    >>> dct = {'Curry': [[38,2,3],[38,5,0]], 'James': [[26,9,3],[26,5,8]], \
    'Tatum': [[35,4,2],[35,5,3]]}
    >>> nba_stats(dct, identity, "turn_over")
    {'Curry': [3, 0], 'James': [3, 8], 'Tatum': [2, 3]}
    >>> dct = {'Green': [[18,4,2],[21,5,6]], 'Harden': [[24,3,5],[26,6,3]], \
    'Poole': [[31,11,2],[12,5,5]]}
    >>> nba_stats(dct, squared, "free_throw")
    {'Green': [16, 25], 'Harden': [9, 36], 'Poole': [121, 25]}
    """
    if stats == 'total_points':
        idx = 0
    elif stats == 'free_throw':
        idx = 1
    elif stats == 'turn_over':
        idx = 2

    return {key: [func(y) for y in [x[idx] for x in values]] \
    for (key, values) in dct.items()}
# Problem 4
def pumpkin_calc(x, y, z):
    """
    >>> pumpkin_calc(1, 2, 3)(1)
    0.04
    >>> pumpkin_calc(3, 4, 5)(50.24)
    0.2
    >>> inner = pumpkin_calc(0.2, 4, 0.8)
    >>> inner(10)
    3.732
    >>> inner(50)
    18.66
    """
    def ppci(w):
        return round(w / (3.14 * x * y * z *4/3), 3)
    return ppci
         

  
  
# Problem 5
def decipher_text(key1, key2, key3):
    """
    >>> inner = decipher_text('Q', 'b', 'C')
    >>> inner('bNswqR')
    'answer'
    >>> inner('jcstbsimplqtqst')
    'justasimpletest'
    >>> inner = decipher_text('W', 'J', 'Z')
    >>> inner('TESTYJZRCJDE')
    'testyourcode'
    >>> inner('ONWTWST') 
    'onetest'
    """
    def decode(x):
        return_str = ''
        for i in x:
            if i.lower() == key1.lower() and x.index(i) % 2 == 1:
                return_str = return_str + 'i'
            elif i.lower() == key1.lower() and x.index(i) %2 == 0:
                return_str = return_str + 'e'
            elif i.lower() == key2.lower() and x.index(i) %2 == 1:
                return_str = return_str + 'o'
            elif i.lower() == key2.lower() and x.index(i) %2 == 0:
                return_str = return_str + 'a'
            elif i.lower() == key3.lower():
                return_str = return_str + 'u'
            else:
                return_str = return_str + i.lower()
        return return_str
    return decode

 
# Problem 6
def grade_calculator(w1,  w2):
    """
    >>> output = grade_calculator(0.4, \
    0.6)
    >>> len(output) == 2
    True
    >>> output[0]((1, 1, 0.5), (1, 1, 1))
    0.93
    >>> output[1]((0.6, 0.7, 0.8), (0.8, 0.8, 0.8))
    'C'
    >>> output[1]((0.5,), (1,))
    'B'
    >>> output[1]((), ())
    'F'
    >>> output[0]((), ())
    0.0
    >>> output[0]((1,), (1,))
    1.0
    >>> output[0]((1,), ())
    0.4
    """

    def rawgrade(x,y):
        if len(x) == 0:
            grade1 = 0
        else:
            grade1 = (sum(x) / len(x))
        if len(y) == 0:
            grade2 = 0
        else:
            grade2 = sum(y) / len(y)
        return round((grade1) * w1 + (grade2) * w2, 2)
    def letter(x,y):
        if rawgrade(x,y) >= 0.9:
            return 'A'
        elif rawgrade(x,y) >= 0.8:
            return 'B'
        elif rawgrade(x,y) >= 0.7:
            return 'C'
        elif rawgrade(x,y) >= 0.6:
            return 'D'
        else:
            return 'F'
    return rawgrade, letter





