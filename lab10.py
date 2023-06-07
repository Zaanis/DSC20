"""
DSC 20 Lab 10
Name: Joshua Chen
PID:  A16810747
"""

# Question 1.1
class Collection:
    """
    A class to abstract the common functionalities of Stack and Queue.
    This class should not be initialized directly.
    """

    def __init__(self):
        """ Constructor. """
        # YOUR CODE GOES HERE #
        self.items = []
        self.num_items = 0

    def size(self):
        """ Get the number of items stored. """
        # YOUR CODE GOES HERE #
        return self.num_items

    def is_empty(self):
        """ Check whether the collection is empty. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return True
        else:
            return False

    def clear(self):
        """ Remove all items in the collection. """
        # YOUR CODE GOES HERE #
        self.items = []
        self.num_items = 0


# Question 1.2
class Stack(Collection):
    """
    Stack class.

    >>> stk = Stack()
    >>> stk.size()
    0
    >>> stk.is_empty()
    True
    >>> str(stk)
    '(bottom) (top)'
    >>> stk.push(None)
    Traceback (most recent call last):
    ...
    ValueError: None is not a valid item
    >>> stk.push('LAB 10')
    >>> stk.size()
    1
    >>> stk.is_empty()
    False
    >>> stk.push('DSC')
    >>> stk.push(20)
    >>> stk.size()
    3
    >>> str(stk)
    '(bottom) LAB 10 -- DSC -- 20 (top)'
    >>> stk.pop()
    20
    >>> stk.pop()
    'DSC'
    >>> stk.peek()
    'LAB 10'
    >>> stk.size()
    1
    >>> stk.clear()
    >>> stk.pop()
    >>> stk.peek()
    """

    def push(self, item):
        """ Push `item` to the stack. """
        # YOUR CODE GOES HERE #
        if item == None:
            raise ValueError('None is not a valid item')
        else:
            self.num_items += 1
            self.items.insert(0, item)
    def pop(self):
        """ Pop the top item from the stack. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return None
        else:
            to_return = self.items[0]
            del self.items[0]
            self.num_items -= 1
            return to_return
    def peek(self):
        """ Peek the top item. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return None
        else:
            return self.items[0]

    def __str__(self):
        """ Return the string representation of the stack. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return "(bottom) (top)"
        else:
            items_string = ' '
            for i in self.items[::-1]:
                items_string += str(i) + ' -- '
            return '(bottom)' + items_string[:-3] + '(top)'


# Question 1.3
class Queue(Collection):
    """
    Queue class.

    >>> que = Queue()
    >>> que.size()
    0
    >>> que.is_empty()
    True
    >>> str(que)
    '(front) (rear)'
    >>> que.enqueue(None)
    Traceback (most recent call last):
    ...
    ValueError: None is not a valid item
    >>> que.enqueue('LAB 10')
    >>> que.size()
    1
    >>> que.is_empty()
    False
    >>> que.enqueue('DSC')
    >>> que.enqueue(20)
    >>> que.size()
    3
    >>> str(que)
    '(front) LAB 10 -- DSC -- 20 (rear)'
    >>> que.dequeue()
    'LAB 10'
    >>> que.dequeue()
    'DSC'
    >>> que.peek()
    20
    >>> que.size()
    1
    >>> que.clear()
    >>> que.dequeue()
    >>> que.peek()
    """

    def enqueue(self, item):
        """ Enqueue `item` to the queue. """
        # YOUR CODE GOES HERE #
        if item == None:
            raise ValueError('None is not a valid item')
        else:
            self.num_items += 1
            self.items.append(item)
    def dequeue(self):
        """ Dequeue the front item from the queue. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return None
        else:
            self.num_items -= 1
            return self.items.pop(0)
    def peek(self):
        """ Peek the front item. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return None
        else:
            return self.items[0]
    def __str__(self):
        """ Return the string representation of the queue. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return "(front) (rear)"
        else:
            items_string = ' '
            for i in self.items:
                items_string += str(i) + ' -- '
            return '(front)' + items_string[:-3] + '(rear)'
