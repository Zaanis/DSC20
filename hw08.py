"""
DSC 20 Fall 2022 Homework 08
Name: Joshua Chen
PID: A16810747
"""

# # Question 1

class DoggyCare:
    """
    >>> t1 = DoggyCare({'daisy': 20, 'wasabi': 10, 'cookie': 30, 'lucky': 40}) 
    >>> t2 = t2 = DoggyCare({'kimchi': 70, 'abby': 90})
    >>> t3 = DoggyCare({'abby': 40, 'pumpkin': 0, 'kimchi': 30, 'mochi': 20})
    >>> t4 = DoggyCare({'abby': 40, 'pumpkin': 0, 'kimchi': 0, 'mochi': 20})
    >>> t1
    {'wasabi': 10, 'daisy': 20, 'cookie': 30, 'lucky': 40}
    >>> print(t1)
    Need to add more food for wasabi! 10 percent of fullness for wasabi now.
    >>> t2 = DoggyCare({'kimchi': 70, 'abby': 90})
    >>> print(t2)
    No dogs to feed yet!
    >>> t1 == t1
    True
    >>> t1 == t3
    True
    >>> t1 == t4
    False
    >>> t1 + t2
    {'wasabi': 10, 'daisy': 20, 'cookie': 30, 'lucky': 40, 'kimchi': 70, \
'abby': 90}
    """
    # YOUR CODE STARTS HERE #
    def __init__(self, dogs):
        self.dogs = dict(sorted(dogs.items(), key = lambda item: item[1]))
    def __repr__(self):
        return str(self.dogs)
    def __str__(self):
        threshold = 30
        if len(self.dogs) == 0:
            return 'NO DOGS TODAY, HAVE A REST!'
        if list(self.dogs.values())[0] > threshold:
            return 'No dogs to feed yet!'
        else:
            return 'Need to add more food for ' + list(self.dogs.keys())[0] +\
            '! ' + str(list(self.dogs.values())[0]) + \
            ' percent of fullness for ' + list(self.dogs.keys())[0] + ' now.'
    def __eq__(self, other):
        self_count = 0
        other_count = 0
        self_amount = 0
        other_amount = 0
        hungry = 30
        difference_threshold = 20
        for i in self.dogs.values():
            if i < hungry:
                self_count += 1
                self_amount += hungry - i
        for i in other.dogs.values():
            if i < hungry:
                other_count += 1
                other_amount += hungry - i
        if self_count != other_count:
            return False
        if abs(self_amount - other_amount) >= difference_threshold:
            return False
        return True
    def __add__(self, other):
        full = 100
        return_dog = DoggyCare(self.dogs)
        for i in range(len(other.dogs.keys())):
            name = list(other.dogs.keys())[i]
            if name in self.dogs:
                return_dog.dogs[name] += other.dogs[name]
                if return_dog.dogs[name] > full:
                    return_dog.dogs[name] = full
            else:
                return_dog.dogs[name] = other.dogs[name]
        return return_dog


# Question 2
def q2_doctests():
    """
    >>> first_order = Order('large tea', 345)
    >>> first_order
    Order: large tea
    >>> order1 = Base('peach tea', 0.5, 325, 0)
    >>> order2 = Base('matcha', 0.7, 420, 1)
    >>> order1
    Base: peach tea
    >>> print(order1)
    0.5 liter of peach tea with 325 calories per liter and 0 ice level
    >>> order1.get_calories_per_object()
    162.5
    >>> order2.get_calories_per_object()
    293.0
    >>> order1 != order2
    True
    >>> order1 >= order2
    False
    >>> order1 < order2
    True
    >>> topping1 = Topping('lychee jelly', 10, 2)
    >>> topping1
    Topping: lychee jelly
    >>> print(topping1)
    Topping lychee jelly: 10 calories with sweetness level of 2
    >>> topping1.get_calories_per_object()
    20


    >>> bev1 = Beverage('Fruity', [order1], [])
    >>> bev2 = Beverage('Green Drink', [order2], [topping1])
    >>> print(bev1)
    Beverage: Fruity
    >>> bev1
    Bases:
    0.5 liter of peach tea with 325 calories per liter and 0 ice level
    Toppings:
    <BLANKLINE>

   >>> bev3 = Beverage('Volcano', [order1, order2], [topping1])
   >>> bev3
   Bases:
   0.5 liter of peach tea with 325 calories per liter and 0 ice level
   0.7 liter of matcha with 420 calories per liter and 1 ice level
   Toppings:
   Topping lychee jelly: 10 calories with sweetness level of 2
   

    >>> bev1 + bev2
    Bases:
    0.5 liter of peach tea with 325 calories per liter and 0 ice level
    0.7 liter of matcha with 420 calories per liter and 1 ice level
    Toppings:
    Topping lychee jelly: 10 calories with sweetness level of 2
    >>> combined_bev1 = bev2 + bev2 + bev1
    >>> combined_bev1.get_total_calories()
    789.5
    >>> combined_bev1
    Bases:
    1.4 liter of matcha with 420 calories per liter and 1 ice level
    0.5 liter of peach tea with 325 calories per liter and 0 ice level
    Toppings:
    Topping lychee jelly: 10 calories with sweetness level of 4
    >>> print(combined_bev1)
    Beverage: Green Drink Green Drink Fruity
    >>> bev3 = Beverage('Empty', [], [])
    >>> bev3.get_total_calories()
    0
    >>> print(bev3)
    Beverage: Empty
    >>> bev3
    Bases:
    <BLANKLINE>
    Toppings:
    <BLANKLINE>
    >>> bev1 + bev3
    Bases:
    0.5 liter of peach tea with 325 calories per liter and 0 ice level
    Toppings:
    <BLANKLINE>
    >>> bev4 = Beverage('Sodium', [order1], [topping1])
    >>> bev1 + bev4
    Bases:
    1.0 liter of peach tea with 325 calories per liter and 0 ice level
    Toppings:
    Topping lychee jelly: 10 calories with sweetness level of 2
    >>> bev2 + bev4
    Bases:
    0.7 liter of matcha with 420 calories per liter and 1 ice level
    0.5 liter of peach tea with 325 calories per liter and 0 ice level
    Toppings:
    Topping lychee jelly: 10 calories with sweetness level of 4
    """
  

class Order:
    """
    A class represents an order from boba shop
    """
    def __init__(self, name, calories):
        """
        Constructor of the Order Class which initialize two instance 
        attributes 
        """
        self.name = name
        self.calories = calories
        # YOUR CODE GOES HERE #
    
    def get_calories_per_object(self):
       # YOUR CODE GOES HERE #
        return self.calories

    def __eq__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_calories_per_object() == \
        other_order.get_calories_per_object():
            return True
        else:
            return False        

    def __ne__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_calories_per_object() != \
        other_order.get_calories_per_object():
            return True
        else:
            return False    

    def __gt__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_calories_per_object() > \
        other_order.get_calories_per_object():
            return True
        else:
            return False 

    def __ge__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_calories_per_object() >= \
        other_order.get_calories_per_object():
            return True
        else:
            return False 

    def __lt__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_calories_per_object() < \
        other_order.get_calories_per_object():
            return True
        else:
            return False

    def __le__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_calories_per_object() <= \
        other_order.get_calories_per_object():
            return True
        else:
            return False


    def __repr__(self):
        """
        return the class name the object is in and the name of the object 
        """
        # You can use this to get the class name of an Order instance, whether
        # it be a Base, or Topping
        class_name = self.__class__.__name__
        # YOUR CODE GOES HERE #
        return class_name + ': ' + self.name
        

class Base(Order):
    """
    A subclass of class Order
    """
    def __init__(self, name, volume, calories, ice_level):
        super().__init__(name, calories)
        self.volume = volume
        self.ice_level = ice_level

    def get_calories_per_object(self):
        # return calories of Base object, volumne * calories - ice_level
        # YOUR CODE GOES HERE #
        return self.volume * self.calories - self.ice_level
    
    def __str__(self):
        # str format:
        # x liter of (name) with y calories per liter and z ice level 
        # YOUR CODE GOES HERE #
        return str(self.volume) + ' liter of ' + self.name + ' with ' + \
        str(self.calories) + ' calories per liter and ' + \
        str(self.ice_level) + ' ice level'

class Topping(Order):
    """
    A subclass of class Order 
    """
    def __init__(self, name, calories, sweetness):
        super().__init__(name, calories)
        self.sweetness = sweetness
    def get_calories_per_object(self):
        # return calories multiplied by sweetness
        # YOUR CODE GOES HERE #
        return self.calories * self.sweetness
    
    def __str__(self):
        # str format:
        # (name): x calories with sweetness level of y
        return self.__class__.__name__+ ' ' + self.name + ': ' + \
        str(self.calories) + ' calories with sweetness level of ' + \
        str(self.sweetness)

class Beverage:
    """
    A class that represent the beverage including bases and toppings that 
    they need
    """
    def __init__(self, name, bases, toppings):
        self.name = name
        self.bases = bases
        self.toppings = toppings
        # YOUR CODE GOES HERE #

    def get_total_calories(self):
        # return total amount of calories of bases and toppings #
        # YOUR CODE GOES HERE #
        total = 0
        for i in self.bases:
            total += i.get_calories_per_object()
        for j in self.toppings:
            total += j.get_calories_per_object()
        return total
       
    
    def __eq__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_total_calories() == other_order.get_total_calories():
            return True
        else:
            return False     

    def __ne__(self, other_order):    
        # YOUR CODE GOES HERE #
        if self.get_total_calories() != other_order.get_total_calories():
            return True
        else:
            return False     

    def __gt__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_total_calories() > other_order.get_total_calories():
            return True
        else:
            return False     

    def __ge__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_total_calories() >= other_order.get_total_calories():
            return True
        else:
            return False     

    def __lt__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_total_calories() < other_order.get_total_calories():
            return True
        else:
            return False     

    def __le__(self, other_order):
        # YOUR CODE GOES HERE #
        if self.get_total_calories() <= other_order.get_total_calories():
            return True
        else:
            return False     

    def __add__(self, other_order):
        # mix one beverage with another to get a new beverage
        # new name of beverage is current + other beverage's name, with space 
        # in between
        # if bases in both recipe, add volume together, take higher calory 
        # between the 2, and higher of the 2 ice levels
        # if same toppings, add their sweetness together
        # YOUR CODE GOES HERE #
        new_bev = Beverage('', [], [])
        new_bev.name = self.name + ' ' + other_order.name
        new_bases = []
        new_toppings = []
        current_bases = [base.name.lower() for base in self.bases]
        current_toppings = [topping.name.lower() for topping in self.toppings]
        for i in other_order.bases:
            other_copy = Base(i.name, i.volume, i.calories, i.ice_level)
            if other_copy.name.lower() in current_bases:
                for j in self.bases:
                    self_copy = Base(j.name, j.volume, j.calories, j.ice_level)
                    if other_copy.name.lower() == self_copy.name.lower():
                        self_copy.volume += other_copy.volume
                        self_copy.calories = max(self_copy.calories, \
                        other_copy.calories)
                        self_copy.ice_level = max(self_copy.ice_level, \
                        other_copy.ice_level)
                        new_bases += [self_copy]
                current_bases.remove(other_copy.name.lower())
            else:
                new_bases += [other_copy]
        for i in self.bases:
            if i.name.lower() in current_bases:
                new_bases = [i] + new_bases
        for i in other_order.toppings:
            other_copy = Topping(i.name, i.calories, i.sweetness)
            if other_copy.name.lower() in current_toppings:
                for j in self.toppings:
                    self_copy = Topping(j.name, j.calories, j.sweetness)
                    if other_copy.name.lower() == self_copy.name.lower():
                        self_copy.sweetness += other_copy.sweetness
                        self_copy.calories = max(self_copy.calories, other_copy.calories)
                        new_toppings += [self_copy]
                current_toppings.remove(other_copy.name.lower())
            else:
                new_toppings += [other_copy]
        for i in self.toppings:
            if i.name.lower() in current_toppings:
                new_toppings = [i] + new_toppings
        new_bev.bases = new_bases
        new_bev.toppings = new_toppings
        return new_bev
             
    def __str__(self):
        # YOUR CODE GOES HERE #
        return self.__class__.__name__ + ': ' + self.name
      
    def __repr__(self):
        # YOUR CODE GOES HERE #
        return_str = 'Bases:' + '\n'
        for i in self.bases:
            return_str += i.__str__() + '\n'
        if return_str[-1] != '\n':
            return_str += '\n'
        return_str += 'Toppings:\n'
        for j in self.toppings:
            if j != self.toppings[-1]:
                return_str += j.__str__() + '\n'
            else:
                return_str += j.__str__()
        if self.bases == [] and self.toppings == []:
            return_str = 'Bases:\n\n' + 'Toppings:\n'
            return return_str
        else:
            return return_str
       