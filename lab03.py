"""
DSC 20 Lab 03
Name: Joshua Chen   
PID: A16810747
"""

# Problem 1.1

def decode_details(filename):
    """
    Decodes message from the given input file.
    ---
    Parameters:
    filename: a string of the filename
    skip: an int representing the number of lines to skip
    ---
    Returns a string of the decoded message
    >>> print(decode_details('files/file1.txt'))
    jack reacher
    23@4 b#l31oo%m@^ way
    FSD@si%m3~on fis#he%r
    121 rockefeller avenue
    32'1 fulleH##r "dr^i~v@e
    @@4:)5#0p1m#
    7/29 06.45
    >>> print(decode_details('files/file2.txt'))
    kurt hendricks
    simon 1p@egg
    @kremlin office
    b%i>%g@ be>n @lond#o&&n
    moscow
    @reykj@av>>ik:/
    12:50 23/11
    >>> print(decode_details('files/file3.txt'))
    <BLANKLINE>
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        new_lines = [x.replace('!', '').replace('?', '').replace(';', \
        '').replace('$', '').strip() for x in lines]
        return_string = ''
        for words in new_lines:
            return_string = return_string + words + '\n'
    return return_string.strip()
    
# Problem 1.2
def decode_details_skipped(filename, skip):
    """
    Decodes message from the given input file and skips through
    certain lines based on the input skip parameter.
    ---
    Parameters:
    filename: a string of the filename
    skip: an int representing the number of lines to skip
    ---
    Returns a string of the decoded message
    >>> print(decode_details_skipped('files/file1.txt', 2))
    jack reacher
    121 rockefeller avenue
    7/29 06.45
    >>> print(decode_details_skipped('files/file2.txt', 1))
    kurt hendricks
    @kremlin office
    moscow
    12:50 23/11
    >>> print(decode_details_skipped('files/file3.txt', 0))
    <BLANKLINE>
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        new_lines = [x.replace('!', '').replace('?', '').replace(';', \
        '').replace('$', '').strip() for x in lines]
    return_string = ''
    i = 0
    while i in range(len(new_lines)):
        return_string = return_string + new_lines[i] + '\n'
        i = i + skip + 1
    return return_string.strip()



# Problem 2
def passcode(filename):
    """
    Counts number of occurences of each alphabet and concatenates counts
    to return a passcode.
    ---
    Parameters:
    filename: filename of file with details required to obtain the passcode
    ---
    Returns the passcode as a string

    >>> passcode('files/pass1.txt')
    '121338121101123642566213'
    >>> (passcode('files/pass2.txt'))
    ''
    >>> passcode('files/pass3.txt')
    '7241311561623328831111'
    """
    with open(filename) as f:
        lines = f.readlines()
        total = ''
        for word in lines:
            total = total + word.strip().lower().replace(' ', '')
        totallist = []
        for letter in total:
            totallist.append(letter)
        dictionary = {}
        for letters in totallist:
            if letters.isalpha() and letters not in dictionary:
                dictionary[letters] = 1
            elif letters.isalpha() and letters in dictionary:
                dictionary[letters] = dictionary.get(letters) + 1
        return_string = str("")
        for ordered in sorted(dictionary):
            return_string = return_string + str(dictionary.get(ordered))
    return return_string

# Problem 3.1
def dollars_cents(lst):
    """
    convert the change to dollar and cent amount
     ---
    Parameters:
    lst: the input changes as a list of integers
    ---
    returns a list of their converted amount
    
    >>> dollars_cents([100, 345])
    ['1 dollar(s) and 0 cents', '3 dollar(s) and 45 cents']
    >>> dollars_cents([3])
    ['0 dollar(s) and 3 cents']
    >>> dollars_cents([])
    []
    >>> dollars_cents([1, 11, 111, 1111])
    ['0 dollar(s) and 1 cents', '0 dollar(s) and 11 cents', '1 dollar(s) \
and 11 cents', '11 dollar(s) and 11 cents']
    """
    return [str(x//100) + ' dollar(s) and ' + str(x%100) + ' cents' \
    for x in lst]



# Problem 3.2  # if
def sum_certain_amount(lst):
    """
    takes a list of integers (representing the change) and returns the total
    amount of money (as dollars) ignoring everything smaller than $50 and 
    discarding the change as well. 
    ---
    Parameters:
    lst: the list of integers representing changes
    ---
    returns the sum dollar amount
    
    >>> sum_certain_amount([30, 345, 5678, 12908])
    185
    >>> sum_certain_amount([30, 345, 56])
    0
    >>> sum_certain_amount([])
    0
    >>> sum_certain_amount([1000, 20000, 4999])
    200
    """
    return sum([0] + [sum([x//100]) for x in lst if x//100 > 50])



# Problem 3.3
def dollars_only(lst):
    """
    takes a tuple of tuples, where each inner tuple contains a positive
    integer and a string, indicating the type of a currency. Return a 
    list with dollar amounts, and a string ‘keep in vault’ for other
    currencies. 
    ---
    Parameters:
    lst: the tuple of tuples representing changes, where each inner tuple
    contains a positive integer and a string, indicating the type of a
    currency.
    ---
    return a list with dollar amounts, and a string ‘keep in vault’ for
    other currencies. 
    
    >>> dollars_only(((200, "dollars"), (480, "euros"), (100, "euros")))
    [200, 'keep in vault', 'keep in vault']
    >>> dollars_only(((5, "euros"), (7, "rubles"), (100, "renminbi")))
    ['keep in vault', 'keep in vault', 'keep in vault']
    >>> dollars_only(((15, "dollars"), (75, "dollars"), (100, "dollars")))
    [15, 75, 100]
    """

    return [x[0] for x in lst if x[1] == 'dollars'] + \
    ['keep in vault' for x in lst if x[1] != 'dollars']


# Problem 3.4
def names_only(names):
    """
    >>> names_only([("Tom", "Cruise"), ("Jon", "Voight"),("Henry", "Czerny")])
    ['Tom', 'Cruise', 'Jon', 'Voight', 'Henry', 'Czerny']
    >>> names_only([()])
    []
    >>> names_only([])
    []
    >>> names_only([("Marina", "Langlois")])
    ['Marina', 'Langlois']
    """
    
    return  [x for i in range(len(names)) for x in names[i]] 


# Problem 4
def name_identify(names):
    """
    IMPORTANT: You should only use list comprehension for this question.
    Follow the syntax guidelines in the writeup.
    input a list of names and return the first name for names with m in its
    last name
    ---
    Parameters:
    names: the list of valid first name 
    ---
    Returns the list of first name
    >>> name_identify(['Marina Langlois', 'James Bond', 'Austin Madden'])
    ['Austin']
    >>> name_identify(['Martina Sampson', 'Jill Gordon', 'Cary Barber'])
    ['Martina']
    >>> name_identify(['Dana Donaldson', 'Selma Owen'])
    []
    """

    return [x.split()[0] for x in names if 'm' in x.split()[1].lower()]


# Problem 5
def message_encoding(message):
    """
    IMPORTANT: You should only use list comprehension for this question.
    Follow the syntax guidelines in the writeup.
    encode a message by shifting every string in that list i steps forward 
    where i is the index of that string
    ---
    Parameters:
    message: the input list of string
    ---
    Returns the encoded message as a list of strings
    >>> message_encoding(['1234', '1234', '1234'])
    ['1234', '2341', '3412']
    >>> message_encoding(['12', '12', '12', '12'])
    ['12', '21', '12', '21']
    >>> message_encoding(['123456', '1', '345', '4'])
    ['123456', '1', '534', '4']
    """

    return [message[i][i%len(message[i])::] + \
    message[i][0:i%len(message[i])] for i in range(len(message))]

