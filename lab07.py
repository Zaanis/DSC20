"""
DSC 20 Fall 2022 Lab 07
Name: Joshua Chen
PID: A16810747
"""

# Question 1
def min_recursion(lst):
    """
    Find the minimum of the list recursively.

    >>> min_recursion([1, 2, 3, 4])
    1
    >>> min_recursion([3, 2, 4, 2])
    2
    >>> min_recursion([6, 7, 8, 2, 5])
    2
    """
    # YOUR CODE GOES HERE #
    if len(lst) == 1:
       return lst[0]
    else:
       minNumber = min_recursion(lst[1:])
       current_min = lst[0]
       if minNumber < current_min:
            current_min = minNumber
       return current_min


# Question 2
def count_chars(s):
    """
    Counts the occurrences of characters and returns a dictionary.
    
    >>> d_1 = count_chars('AaBb*A')
    >>> dict(sorted(d_1.items()))
    {'*': 1, 'A': 2, 'B': 1, 'a': 1, 'b': 1}

    >>> d_2 = count_chars('dsc20_FA22')
    >>> dict(sorted(d_2.items()))
    {'0': 1, '2': 3, 'A': 1, 'F': 1, '_': 1, 'c': 1, 'd': 1, 's': 1}

    >>> count_chars('')
    {}
    """
    # YOUR CODE GOES HERE #
    dct = {}
    if len(s) == 0:
        return dct
    else:
        dct = count_chars(s[1:])
        if s[0] in dct:
            dct[s[0]] += 1
        else:
            dct[s[0]] = 1
        return dct   


# Question 3
def merge(lst_1, lst_2):
    """
    Merges two sorted lists into a sorted output list.

    >>> merge([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([], [1, 2, 3, 4])
    [1, 2, 3, 4]
    """
    # YOUR CODE GOES HERE #
    if len(lst_1) == 0:
        return lst_2
    elif len(lst_2) == 0:
        return lst_1
    else:
        if lst_1[0] > lst_2[0]:
            return [lst_2[0]] + merge(lst_1, lst_2[1:])
        elif lst_1[0] < lst_2[0]:
            return [lst_1[0]] + merge(lst_1[1:], lst_2)
        elif lst_1[0] == lst_2[0]:
            return [lst_1[0]] + merge(lst_1[1:], lst_2)


# Question 4
def split(*nums, n):
    """
    Splits list by n, n-1, n-2, ..., stops when n=0 or not enough numbers
    are left.

    >>> split(1, 2, 3, 4, 5, n=2)
    [[1, 2], [3]]
    >>> split(1, 2, 3, 4, 5, 6, n=3)
    [[1, 2, 3], [4, 5], [6]]
    >>> split(5, 7, 8, 9, 10, 11, 12, 15, n=4)
    [[5, 7, 8, 9], [10, 11, 12]]
    """
    x = list(nums)
    if n == 1:
        return [[x[0]]]
    elif len(x) == n:
        return [x]
    elif len(x) < n:
        return []
    else:
        return [x[0:n]] + split(*nums[n:], n = n - 1)


# Question 5
class Pokemon:
    """
    Implementation of a Pokemon class

    >>> gengar = Pokemon('Gengar', 'Ghost and Poison', \
    ['Confuse Ray', 'Shadow Ball'])
    >>> gengar.name
    'Gengar'
    >>> gengar.pokemon_type
    'Ghost and Poison'
    >>> gengar.moves
    ['Confuse Ray', 'Shadow Ball']
    >>> gengar.take_movement(5)
    'Fail to take the movement'
    >>> gengar.take_movement(0)
    'Confuse Ray'
    >>> gengar.show_total_moves()
    'The total moves of Gengar is 1'

    >>> fake = Pokemon('NoName', 'Fake', [])
    >>> fake.show_total_moves()
    'The total moves of NoName is 0'
    """
    # TODO: Uncomment structure below and fill in the blanks
    def __init__(self, name, pokemon_type, moves):
        self.name = name
        self.pokemon_type = pokemon_type
        self.moves = moves
        self.total_moves = 0  # track total moves
    
    def take_movement(self, idx):
        if idx > len(self.moves):
            return 'Fail to take the movement'
        else:
            self.total_moves += 1
            return self.moves[idx]
    
    def show_total_moves(self):
        return 'The total moves of ' + self.name + ' is ' + \
            str(self.total_moves)


# Question 6
class Student:
    """
    Implementation of Student
    """
    # YOUR CODE GOES HERE #
    describe = 'This is a student account'
    def edit_canvas():
        return 'Student account cannot edit this course'
    def __init__(self, pid, height, dob, gpa):
        self.pid = pid
        self.height = height
        self.dob = dob
        self.gpa = gpa
    def info(self):
        return 'The student ' + self.pid + " was born on " + self.dob + \
            ". The student has a gpa of " + str(self.gpa)
    def get_gpa(self):
        return self.gpa
    def set_gpa(self, new_grade):
        if new_grade < 0 or new_grade > 4:
            return 'Invalid Input'
        else:
            self.gpa = new_grade
            return True


def doctest_q6():
    """
    >>> s1 = Student("A123456", 180.2, "2022-10-22", 3.8)
    >>> s1.describe
    'This is a student account'
    >>> s1.pid
    'A123456'
    >>> s1.height
    180.2
    >>> s1.dob
    '2022-10-22'
    >>> s1.get_gpa()
    3.8
    >>> s1.set_gpa(2.6)
    True
    >>> s1.gpa
    2.6
    >>> s1.set_gpa(-5)
    'Invalid Input'
    >>> s1.info()
    'The student A123456 was born on 2022-10-22. \
The student has a gpa of 2.6'

    >>> s2 = Student("A12", 175.4, "2000-10-22", 3.5)
    >>> s2.describe
    'This is a student account'

    >>> Student.edit_canvas()
    'Student account cannot edit this course'
    """
    return
    