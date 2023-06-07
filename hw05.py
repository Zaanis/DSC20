"""
DSC 20 Fall 2022 Homework 05
Name: Joshua Chen
PID: A1681074
"""
# Helper function
def round_up(x, y):
    """
    automatically rounds up from x/y if remainer is not 0
    >>> round_up(5, 5)
    1
    >>> round_up(6, 5)
    2
    >>> round_up(0, 5)
    0
    >>> round_up(4, 5)
    1
    """
    if x % y == 0:
        return x // y
    else:
        return (x // y) + 1


# Question1.1
def number_of_trainers_1(lst, level = 20):
    """
    ##############################################################
    take a list of levels, default parameter level = 20
    return number of trainers needed
    ##############################################################
    Every 5 young pokemons with levels lower or equal to the given level
    threshold need 1 trainer.
    >>> number_of_trainers_1([1,2,3,4,5,6,7])
    2
    >>> number_of_trainers_1([1,2,3,4,5,6,7], 5)
    1
    >>> number_of_trainers_1([1,2,3,4,5,6,7], level = 2)
    1
    >>> number_of_trainers_1([100, 200, 300])
    0
    >>> number_of_trainers_1([100, 200, 300], 500)
    1
    >>> number_of_trainers_1([1, 2, 3, 4, 5], 10)
    1
    """
    size = 5
    return round_up(len([x for x in lst if x <= level]), size)


# Question1.2
def number_of_trainers_2(*args):
    """
    ##############################################################
    take an unknown number of levels, level set to 20
    return number of trainers needed
    ##############################################################
    Every 5 young pokemons with levels lower or equal to the given level
    threshold need 1 trainer.
    >>> number_of_trainers_2(1,2,3,4,5,6,7)
    2
    >>> number_of_trainers_2(10,20,13,4)
    1
    >>> number_of_trainers_2(21, 22)
    0
    >>> number_of_trainers_2(100, 200, 300)
    0
    >>> number_of_trainers_2(100, 200, 300, 400, 19)
    1
    >>> number_of_trainers_2(1, 2, 3, 4, 5, 50)
    1
    """
    level = 20
    size = 5
    return round_up(len([x for x in args if x <= level]), size)


# Question1.3
def number_of_trainers_3(*args, level = 20):
    """
    ##############################################################
    take an unknown number of levels, level default set to 20
    return number of trainers needed
    ##############################################################
    Every 5 young pokemons with levels lower or equal to the given level
    threshold need 1 trainer.
    >>> number_of_trainers_3(1,2,3,4,5,6,7)
    2
    >>> number_of_trainers_3(1,2,3,4,5,6,7, level = 5)
    1
    >>> number_of_trainers_3(1,2,3,4,5,6,7, level = 2)
    1
    >>> number_of_trainers_3(100, 200, 300, level = 200)
    1
    >>> number_of_trainers_3(1, 2, 3, 4, 5, 50)
    1
    >>> number_of_trainers_3(1, 2, 3, 4, 5, 50, level = 51)
    2
    """
    size = 5
    return round_up(len([x for x in args if x <= level]), size)


# Question2
def guild_trip(level_limit, **kwargs):
    """
    ##############################################################
    takes a keyword arguments where key is trainer name, value is
    level. Return (name, number of trainers) as a dictionary
    ##############################################################
    take in a level limit and a dictionary, return a dictionary with the number
    of trainers need for each group
    >>> guild_trip(14, ash=[1,2,3], misty =[4,5,6,7], brock=[15,16])
    {'ash': 1, 'misty': 1, 'brock': 0}
    >>> guild_trip(14, ash=[21,3], misty =[41,1,2,24,6,5,7],\
     brock=[30,3,1,7,88])
    {'ash': 1, 'misty': 1, 'brock': 1}
    >>> guild_trip(100, ash=[21,3], misty =[41,1000,2,24,6,99,50],\
     brock=[3,1,7,88,99,100])
    {'ash': 1, 'misty': 2, 'brock': 2}
    >>> guild_trip(0, ash=[1,2,3], misty =[4,5,6,7], brock=[15,16])
    {'ash': 0, 'misty': 0, 'brock': 0}
    >>> guild_trip(14, ash=[1], misty =[19], brock=[13,16])
    {'ash': 1, 'misty': 0, 'brock': 1}
    >>> guild_trip(100, ash=[1,2,3,4,5,6], misty =[4,5,6,7], brock=[2000])
    {'ash': 2, 'misty': 1, 'brock': 0}
    """
    return {k: number_of_trainers_1(i, level_limit) for \
    (k,i) in kwargs.items()}


# Question3
def swap_values(*args, **kwargs):
    """
    ##############################################################
    combine args and kwargs into list of tuples
    tuple contain type of argument, position of argument in args/kwargs
    value the opposing argument holds
    ##############################################################
    >>> swap_values(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', [25, 30]), ('positional_1', [5, 50]), \
('keyword_0_player1', 10), ('keyword_1_player2', False)]
    >>> swap_values('pikachu', ability='thunder jolt')
    [('positional_0', 'thunder jolt'), ('keyword_0_ability', 'pikachu')]
    >>> swap_values(no_positional=True)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> swap_values()
    []
    >>> swap_values(10, 20, 30, no_positional=True, a=10)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> swap_values('a', b='c')
    [('positional_0', 'c'), ('keyword_0_b', 'a')]
    >>> swap_values(1, 2, 3, a=[5], b=[7], c=[9])
    [('positional_0', [5]), ('positional_1', [7]), ('positional_2', [9]), \
('keyword_0_a', 1), ('keyword_1_b', 2), ('keyword_2_c', 3)]
    """
    assert len(args) == len(kwargs)
    return [('positional_' + str(x[0]), x[1]) for x in \
    list(enumerate(kwargs.values()))] + [('keyword_' + \
    str(list(enumerate(args))[i][0]) + "_" + \
    list(kwargs.keys())[i], args[i]) for i in \
    range(len(list(enumerate(args))))]


# Question 4
def pokemon_comp(**kwargs):
    """
    ##############################################################
    takes in unknown number of (name: levels), produce an energy list
    with each pokemon's calculated energy. pokemon_comp return inner function
    that takes threshold value and copmares with the sum of energy list.
    ##############################################################
    >>> diff1 = pokemon_comp(Alcremie=34, Happiny=49, Zapdos=70)
    >>> diff1(123)
    806
    'Zapdos'
    >>> diff1(444456)
    147
    'Happiny'
    >>> diff1(1119)
    373
    >>> pokemon_comp(Bagon=55, Pikachu=100)(1234)
    300
    'Bagon'
    >>> diff1(0)
    806
    'Zapdos'
    >>> diff1(10000000)
    147
    'Happiny'
    >>> pokemon_comp(Bagon=55, Pikachu=100)(749)
    374
    """
    aggron_attack = 10
    alcremie_attack = 3
    bagon_attack = 5
    bayleef_attack = 4
    happiny_attack = 2
    pikachu_attack = 4
    quagsire_attack = 7
    zapdos_attack = 11
    attack_values = {'Aggron': aggron_attack, 'Alcremie': alcremie_attack,\
        'Bagon': bagon_attack, 'Bayleef': bayleef_attack, 'Happiny': \
        happiny_attack, 'Pikachu': pikachu_attack, 'Quagsire': \
        quagsire_attack, 'Zapdos': zapdos_attack}
    pokemon_and_attack = list(kwargs.items())
    squared = 2
    energy = [pokemon_and_attack[i][1] * attack_values.get(pokemon_and_attack \
    [i][0]) + len(pokemon_and_attack[i][0]) ** squared \
    for i in range(len(pokemon_and_attack))]
    def inner(x):
        """
        if sum of energy > x, print the highest energy and return the
        pokemon's name
        if sum of energy < x, print the lowest energy and return the pokemon's 
        name
        if sum of energy = x, return average of energy list
        """
        if sum(energy) > x:
            print(max(energy))
            return list(kwargs.keys())[energy.index(max(energy))]
        elif sum(energy) < x:
            print(min(energy))
            return list(kwargs.keys())[energy.index(min(energy))]
        else:
            return int(sum(energy) / len(energy))
    return inner


# Question 5
def next_move(file_names, row, col):
    """
    ##############################################################
    takes in a file with each line having information P1, P2, P3
    function will go through each line and remove specified persons 
    according to the following rules:
    1. remove P1 means P2, P3 will stay
    2. remove P2 means P1 will stay and P3 will leave
    3. remove P3 means P1, P2 will stay
    ##############################################################
    >>> message = next_move("files/names.txt", 2, 2)
    >>> message(True)
    71
    >>> message(False)
    'odd'
    >>> message = next_move("files/names.txt", 4, 1)
    >>> message(True)
    85
    >>> message(False)
    'even'
    >>> message = next_move("files/names.txt", 1, 1)
    >>> message(True)
    85
    >>> message(False)
    'even'
    >>> message = next_move("files/names.txt", 3, 2)
    >>> message(True)
    71
    >>> message(False)
    'odd'
    """
    with open(file_names) as f:
        second_person = 2
        lines = []
        for i in f:
            lines.append(i.strip())
        newline = []
        for i in lines:
            newline.append(i.split(','))
        remaining = []
        for i in newline:
            for l in i:
                if l not in remaining:
                    remaining.append(l)
        original_length = len(remaining)
        to_remove = [newline[row - 1][col - 1]]
        newline = newline[row - 1:] + newline[0:row - 1]
        no_remove = []
        while len(to_remove) > 0:
            for i in newline:
                if to_remove[0] in i and to_remove[0] not in no_remove:
                    if i.index(to_remove[0]) == 1:
                        to_remove.append(i[second_person])
                    elif i.index(to_remove[0]) == 0:
                        no_remove.append(i[1])
                        no_remove.append(i[second_person])
                    elif i.index(to_remove[0]) == second_person:
                        no_remove.append(i[0])
                        no_remove.append(i[1])
            remaining.remove(to_remove[0])
            to_remove.remove(to_remove[0])
            newline.remove(i)
        new_length = len(remaining)
    def inner(stats):
        """
        inner function that takes True or False as parameter.
        If True, return the percent of players remaining.
        If False, return whether remaining amount is even or odd
        """
        if stats == True:
            convert_to_percent = 100
            return int(convert_to_percent * new_length / original_length)
        else:
            odd_checker = 2
            if new_length % odd_checker == 1:
                return 'odd'
            else:
                return 'even'
    return inner
     

# Question 6
def message_enc(filepath):
    """
    ##############################################################
    takes a file with only alphanumeric characters and find frequency
    of each character. Function will return an inner function that takes in
    integer i and outfile and swaps ith most frequent characters 
    with ith least frequent and write it into the outfile.
    ##############################################################
    >>> message = message_enc("files/message.txt")
    >>> message(0, 'files/message_swapped.txt')
    >>> with open('files/message_swapped.txt') as f:
    ...     print(f.read())
    AAAAA  AAa     a aaa
    b b bb c cq wert
    >>> message(2, 'files/message_swapped.txt')
    >>> with open('files/message_swapped.txt') as f:
    ...     print(f.read())
    eeeee  eeq     q qqq
    b b bb c ca wArt
    >>> message(5, 'files/message_swapped.txt')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> message = message_enc('files/a.txt')
    >>> message(0, 'files/b.txt')
    >>> with open('files/b.txt') as f:
    ...     print(f.read())
    Oompa Loompa
    >>> message(10, 'files/b.txt')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> message(2, 'files/b.txt')
    >>> with open('files/b.txt') as f:
    ...     print(f.read())
    pLmOa oLLmOa
    """
    with open(filepath) as f:
        lines = []
        for i in f:
            lines.append(i.strip())
        new_dict = {}
        for line in lines:
            for letter in line:
                if letter != ' ':
                    if letter not in new_dict:
                        new_dict[letter] = 1
                    else:
                        new_dict[letter] += 1 
        sorted_dict = dict(sorted(new_dict.items(), key = lambda item:\
        item[1]))
        reverse_sorted = {}
        for k, v in sorted_dict.items():
            if v not in reverse_sorted:
                reverse_sorted[v] = [k]
            else:
                reverse_sorted[v] = reverse_sorted[v] + [k]
    def inner(i, outfile):
        """
        inner function that will swap the i time the ith most
        frequent letter with ith least frequent letter and write it into
        another file.
        """
        replace_list = []
        for letters in reverse_sorted.values():
            replace_list = replace_list + sorted(letters)
        half = 0.5
        assert i <= half * len(replace_list)
        while i > 0:
            to_replace1 = replace_list[i - 1]
            to_replace2 = replace_list[len(replace_list) - i]
            for line in lines:
                line_copy = list(line)
                to_replace1_index = []
                to_replace2_index = []
                for j in range(len(line)):
                    if line[j] == to_replace1:
                        to_replace1_index.append(j)
                    elif line[j] == to_replace2:
                        to_replace2_index.append(j)
                for letter_index in to_replace1_index:
                    line_copy[letter_index] = to_replace2
                for letter_index in to_replace2_index:
                    line_copy[letter_index] = to_replace1
                return_str = ""
                for letters in line_copy:
                    return_str = return_str + letters
                lines[lines.index(line)] = return_str
            i -= 1
        for j in range(len(lines)):
            if j != len(lines) - 1 and "\n" not in lines[j]:
                lines[j] = lines[j] + "\n"
            else:
                lines[j] = lines[j]
        with open(outfile, 'w') as f:
            for line in lines:
                f.write(line)
    return inner