"""
DSC 20 Homework 09
Name: Joshua Chen
PID:  A16810747
"""


# Question 1
def check_brackets(string):
    """
    ##############################################################
    recursive function that takes string and check whether or not
    it contain correct set of nested brackets, only 3 possible types
    (), {}, []
    ##############################################################
    
    >>> check_brackets("()")
    True
    >>> check_brackets("(())")
    True
    >>> check_brackets("[{()}]")
    True
    >>> check_brackets("(){}")
    False
    >>> check_brackets("[(()])")
    False
    >>> check_brackets("({x}))")
    False
    >>> check_brackets("[(x)]")
    False
    >>> check_brackets("")
    True

    # Add at least 3 doctests below here #
    >>> check_brackets("{}")
    True
    >>> check_brackets('(aa)')
    False
    >>> check_brackets('( )')
    False
    """
    if len(string) == 0:
        return True
    else:
        if (string[0], string[-1]) in [('(', ')'), ('{', '}'), ('[', ']')]:
            return check_brackets(string[1:-1])
        else:
            return False
# Q2 No doctests or docstrings are needed. Fix the code. 

# Question 2.1
def fix_concat_str(lst1, lst2):
    """
    Concatenate all of the elements in `lst1` with each element in `lst2`
    and return the values in a list.

    >>> fix_concat_str(["so", "how", {"`was`"}], ["your", 10, "day?"])
    ['soyour', 'howyour', 'soday?', 'howday?']
    >>> fix_concat_str([], [])
    []
    >>> fix_concat_str(["a", "b", "c"], ["1", "2", "3", "4"])
    ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3', 'a4', 'b4', 'c4']
    """
    out = []
    for str2 in lst2:
        for str1 in lst1:
            try:
                out.append(str1 + str2)
            except:
                continue  # add try-except block
    return out


# Question 2.2
def fix_open_file(*filepaths):
    """
    Open all of the files in `filepaths` and PRINT a string for each file
    that indicates if this file can be opened or not.

    >>> fix_open_file('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened successfully
    files/b.txt not found
    files/c.txt not found

    >>> fix_open_file('docs.txt')
    docs.txt not found
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r")
            print(filepath + ' opened successfully') # add try-except block
            cur_file.close()
        except:
            print(filepath + ' not found')


# Question 2.3
def fix_add_backwards(lst):
    """
    For each element in `lst`, add it with its previous element
    in the list. Returns all of the summed values in a list.

    >>> fix_add_backwards([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []

    >>> fix_add_backwards([1, 2, 3, 4])
    <class 'IndexError'>
    [5, 3, 5, 7]

    >>> fix_add_backwards([])
    <class 'IndexError'>
    []
    """
    sum_of_pairs = []
    for i in range(len(lst) + 1):
        try:
            sum_of_pairs.append(lst[i] + lst[i - 1]) # add try-except block
        except Exception as e:
            print(type(e))
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    ##############################################################
    check correctness of input1 and input2 using exceptions
    if check fails, throw exception
    input1 should be string, all lowercase
    input2 should be a list, should contain input1
    all check pass, return 'input validated'
    ##############################################################

    >>> check_inputs('hi', ['hi', 'doing good?'])
    'Input validated'
    >>> check_inputs('hi', [])
    Traceback (most recent call last):
    ...
    TypeError: input1 not in input2
    >>> check_inputs('hIII', 1)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 1 is not lowercase letter
    >>> check_inputs(1, [1, 2, 'hi'])
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs('hi', 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type

    # Add at least 3 doctests below here #
    >>> check_inputs('hi', ['hi', 50, 60])
    'Input validated'
    >>> check_inputs(50, 60)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs('hi', (50, 60, 'hi'))
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    """
    # Your code is here
    if type(input1) != str:
        raise TypeError('input1 is not the correct type')
    for i in range(len(input1)):
        if input1[i].islower() == False:
            raise TypeError('The element at index ' + str(i) + \
                ' is not lowercase letter')
    if type(input2) != list:
        raise TypeError('input2 is not the correct type')
    if input1 not in input2:
        raise TypeError('input1 not in input2')
    else:
        return 'Input validated'
    


# Question 4
def load_file(filepaths):
    """
    ##############################################################
    check correctness of filepaths
    filepaths should be a list
    each filepath in failpaths should be string
    filepath should be a valid filepath
    all filepath not empty and should only contain alphabets and spaces
    all check pass, return total number of words in all files
    ##############################################################

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filepaths is not a list
    >>> load_file(['files/empty.txt', 1])
    Traceback (most recent call last):
    ...
    TypeError: The filepath at index 1 is not a string
    >>> load_file(['files/ten_words.txt'])
    10
    >>> load_file(['files/ten_words.txt', 'files/empty.txt', 'hah'])
    Traceback (most recent call last):
    ...
    FileNotFoundError: The filepath at index 2 does not exist
    >>> load_file(['files/ten_words.txt', 'files/empty.txt'])
    Traceback (most recent call last):
    ...
    ValueError: The filepath at index 1 is empty or contain non-alphabets
    >>> load_file(['files/ten_words.txt', 'files/nonalpha.txt'])
    Traceback (most recent call last):
    ...
    ValueError: The filepath at index 1 is empty or contain non-alphabets

    # Add at least 3 doctests below here #
    >>> load_file(['files/nonalpha.txt'])
    Traceback (most recent call last):
    ...
    ValueError: The filepath at index 0 is empty or contain non-alphabets
    >>> load_file(['files/ten_words.txt', 'files/ten_words.txt'])
    20
    >>> load_file([['hello']])
    Traceback (most recent call last):
    ...
    TypeError: The filepath at index 0 is not a string
    """
    # Your code is here
    if type(filepaths) != list:
        raise TypeError('filepaths is not a list')
    for i in range(len(filepaths)):
        if type(filepaths[i]) != str:
            raise TypeError('The filepath at index ' + str(i) + \
            ' is not a string')
    for i in range(len(filepaths)):
        try:
             f = open(filepaths[i], "r")
             f.close()
        except:
            raise FileNotFoundError('The filepath at index ' + str(i) + \
                ' does not exist')
    count = 0
    for i in range(len(filepaths)):
        with open(filepaths[i]) as f:
            lines = f.readlines()
            if len(lines) == 0:
                raise ValueError('The filepath at index ' + str(i) + \
                    ' is empty or contain non-alphabets')
            for j in lines:
                if '\n' in j:
                    j = j.replace('\n', '')
                content = j.split(' ')
                for word in content:
                    if word.isalpha() == False:
                        raise ValueError('The filepath at index ' + str(i) + \
                            ' is empty or contain non-alphabets')
                count += len(content)
    return count