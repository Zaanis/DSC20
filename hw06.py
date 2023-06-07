"""
DSC20 FA22 HW06
Name: Joshua Chen
PID:  A16810747
"""

# Question 1
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function. You don't need to add new doctests for this function.
    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 8 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-8, duplicates allowed) #
    # Your code starts here
    return [3, 4, 6, 5, 3, 6, 2, 6, 3, 3]


#Question 2
def candy_num(bag, fav):
    """
    ##############################################################
    use recursion that takes a list of candies you have and a list
    of candies you like, count and return number of your favorite 
    candies
    ##############################################################

    >>> bag = ["Skittles", "M&M", "Hershey","Snickers", "Skittles"]
    >>> candy_num(bag, ["Skittles"])
    2
    >>> candy_num(bag, [])
    0
    >>> candy_num(bag, ["Skittles", "Hershey"])
    3

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> candy_num(bag, ['Hershey'])
    1
    >>> candy_num(bag, ['bananas', 'Snickers'])
    1
    >>> candy_num(['a', 'b', 'c', 'd', 'a' ,'a', 'a', 'a', 'a'], ['a', 'b'])
    7
    """
    # Your code starts here
    if len(bag) == 0:
        return 0
    else:
        if fav.count(bag[0]) > 0:
            return 1 + candy_num(bag[1:], fav)
        else:
            return 0 + candy_num(bag[1:], fav)
    

#Question 3
def count_left_path(left, right):
    """
    ##############################################################
    recursive function that counts how many times going left is more beneficial
    more beneficial if corresponding value from left list is strictly
    greater than value from right list
    ##############################################################

    >>> count_left_path([9,0,2,1,0], [5,2,5,7,8])
    1
    >>> count_left_path([3,2,1], [1,1,5])
    2
    >>> count_left_path([4],[8])
    0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> count_left_path([1, 2, 3], [3, 4, 6])
    0
    >>> count_left_path([4, 4, 4], [4, 4, 4])
    0
    >>> count_left_path([4, 4, 4], [3, 3, 3])
    3
    """
    # Your code starts here
    if len(left) == 0 or len(right) == 0:
        return 0
    else:
        if left[0] > right[0]:
            return 1 + count_left_path(left[1:], right[1:])
        else:
            return 0 + count_left_path(left[1:], right[1:])


#Question 4
def generate_passcode(string):
    """

    ##############################################################
    recursive function that takes input string of word and returns
    passcode, which is length of each word concacenated together
    ##############################################################

    >>> generate_passcode("hello world it's me")
    '5542'
    >>> generate_passcode("can you generate a passcode")
    '33818'
    >>> generate_passcode("")
    '0'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> generate_passcode('i i i i i')
    '11111'
    >>> generate_passcode('hi hi hi hi hi hi hi hi')
    '22222222'
    >>> generate_passcode('i ii iii iiiii iiiiii')
    '12356'
    """
    # Your code starts here
    if string.count(' ') == 0:
        return str(len(string))
    else:
        position = string.find(' ')
        return str(len(string[0:position])) + \
        generate_passcode(string[position + 1:])
    


#Question 5
def pumpkin_to_friend(bag, num):
    """
    ##############################################################
    recursive function that takes list of pumpkin weights as integers
    and number of pumpkins you want to give each friend,
    return list of integers where each integer is sum of the
    weight of the pumpkins for each friend. If not enough pumpkins, do nothing
    ##############################################################

    >>> pumpkin_to_friend([2, 4, 6, 7, 3, 1], 3)
    [12, 11]
    >>> pumpkin_to_friend([2, 4, 6, 7, 3, 1], 4)
    [19]
    >>> pumpkin_to_friend([2, 4, 6, 7, 3, 1], 1)
    [2, 4, 6, 7, 3, 1]
    >>> pumpkin_to_friend([], 3)
    []

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> pumpkin_to_friend([1, 1, 1, 1, 1, 1, 1, 1], 4)
    [4, 4]
    >>> pumpkin_to_friend([2, 2, 2, 2, 2, 2, 2], 100)
    []
    >>> pumpkin_to_friend([100, 1, 2, 100, 1, 2], 2)
    [101, 102, 3]
    """
    # Your code starts here
    if len(bag) < num:
        return []
    else:
        return [sum(bag[0:num])] + pumpkin_to_friend(bag[num:], num)


#Question 6
def expand_formula(compressed_form):
    """
    ##############################################################
    recursive function to output molecule expanded form.
    molecule encloed in {} and coefficient is how many times the molecule 
    will have to be printed.
    ##############################################################

    >>> expand_formula('1{Na}3{C}11{N}5{Co}')
    'NaCCCNNNNNNNNNNNCoCoCoCoCo'
    >>> expand_formula('')
    ''
    >>> expand_formula('6{C}8{H}6{O}')
    'CCCCCCHHHHHHHHOOOOOO'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> expand_formula('6{C}')
    'CCCCCC'
    >>> expand_formula('1{a}1{b}1{c}1{d}1{e}')
    'abcde'
    >>> expand_formula('10{a}1{b}')
    'aaaaaaaaaab'
    """
    # Your code starts here
    if compressed_form.count('}') == 1:
        index = compressed_form.find('}')
        string = compressed_form[0:index]
        print_list = string.split('{')
        return int(print_list[0]) * print_list[1]
    elif compressed_form.count('}') == 0:
        return ''
    else:
        index = compressed_form.find('}')
        string = compressed_form[0:index]
        print_list = string.split('{')
        return int(print_list[0]) * print_list[1] + \
        expand_formula(compressed_form[index + 1:])