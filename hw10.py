"""
DSC 20 Homework 10
Name: Joshua Chen
PID: A16810747
"""

from util import Stack, Queue

# Question 1
def is_duplicated(expression):
    """
    ##############################################################
    Use stack to see whether or not an expression has duplicate parenthesis
    ##############################################################
    
    >>> is_duplicated("((x))")
    True
    >>> is_duplicated("(a+b)+((x))")
    True
    >>> is_duplicated("(a+(b))")
    False
    >>> is_duplicated("(((a+b)))")
    True
    >>> is_duplicated("(a+b)+(c+d)")
    False

    # Add at least 3 doctests below #
    >>> is_duplicated("(a+(b+c))")
    False
    >>> is_duplicated("((a+b+c))")
    True
    >>> is_duplicated("((a))")
    True
    >>> is_duplicated('()+()')
    False
    """
    # YOUR CODE GOES HERE #
    stk = Stack()
    duplicate = 0
    value = False
    check1 = False
    check2 = False
    for i in expression:
        if i == '(' or i == ')':
            stk.push(i)
            value = False
        else:
            if not value:
                stk.push(i)
            value = True
    count = stk.num_items
    for i in range(count):
        if duplicate == 0:
            check1 = False
        if stk.peek() == ')':
            duplicate += 1
            stk.pop()
            value = False
        elif stk.peek() == '(':
            duplicate -= 1
            stk.pop()
            if check1 and not value:
                check2 = True
            if value and duplicate >= 1:
                check1 = True
            value = False
        else:
            stk.pop()
            value = True
    return check2
    

# Question 2
def find_kth_element(k, iterable):
    """
    ##############################################################
    A function that takes interable object and find kth element inside 
    of it using Queue.
    ##############################################################

    >>> find_kth_element(2, [0, 1, 2, 3])
    1
    >>> find_kth_element(4, [0, 1, 2, 3])
    3
    >>> find_kth_element(5, [0, 1, 2, 3])
    0
    >>> find_kth_element(6, [0, 1, 2, 3])
    1

    # Add at least 3 doctests below #
    >>> find_kth_element(10, [0])
    0
    >>> find_kth_element(10, [1,2])
    2
    >>> find_kth_element(1, [1])
    1
    """
    # YOUR CODE GOES HERE #
    que = Queue()
    for i in iterable:
        que.enqueue(i)
    while k > 0:
        if que.peek() == None:
            for i in iterable:
                que.enqueue(i)
            value = que.peek()
            que.dequeue()
        else:
            value = que.peek()
            que.dequeue()
        k -= 1
    return value

# Question 3 (Extra Credit)
def choices_choices(candidate, pattern, possibility):
    """
    Append all possible words to possibility list.

    >>> p = []
    >>> choices_choices(['t','p','h'], "_ower", p)
    >>> p
    ['tower', 'power', 'hower']

    >>> p = []
    >>> choices_choices(['w','c','d'], "_o_er", p)
    >>> p
    ['wocer', 'woder', 'cower', 'coder', 'dower', 'docer']

    >>> p = []
    >>> choices_choices(['w','c','d'], "coder", p)
    >>> p
    ['coder']
    """
    # YOUR CODE GOES HERE #        
    if '_' not in pattern:
        possibility.append(pattern)
    else:
        for i in candidate:
            copy = list(candidate)
            copy.remove(i)
            choices_choices(copy, pattern.replace('_', i, 1), possibility)