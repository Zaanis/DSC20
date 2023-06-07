"""
DSC 20 Lab 08
Name: Joshua Chen
PID:  A16810747
"""
import random


# Question 1

def q1_doctests():
    """
    >>> Player_One = Player("Player_One", "NA")
    >>> Player_Two = RegularPlayer("Player_Two", "EU")
    >>> Player_Three = PremiumPlayer("Player_Three", "CH")
    >>> random.seed(10)
    >>> Player_One.play()
    'Player_One played a game. You won! You have gained 5000 experience points.'
    >>> Player_One.experience
    5000
    >>> print(Player_Two.play_several(3))
    Player_Two played a game. You lost! You have gained 3000 experience points.
    Player_Two played a game. You lost! You have gained 3000 experience points.
    Player_Two played a game. You won! You have gained 5000 experience points.
    >>> Player_Two.experience
    11000
    >>> Player_Two.level_up()
    'Promoted to level 1'
    >>> Player_Two.level
    1
    >>> Player_Two.level_up()
    'Not enough experience!'
    >>> Player_Three.experience
    1000
    >>> print(Player_Three.play_several(2))
    Player_Three played a game. You won! You have gained 5000 experience points.
    Player_Three played a game. You lost! You have gained 3000 experience points.
    >>> Player_Three.experience
    9000
    >>> Player_Three.promote()
    'Promoted to level 1'
    >>> Player_Three.level
    1
    >>> Player_Three.experience
    10000
    """
    return

def doctests():
    """

    """
    return
class Player:
    def __init__(self, username, region):
        # YOUR CODE STARTS HERE #
        self.username = username
        self.region = region
        self.experience = 0
        self.level = 0
        return

    def play(self):
        # YOUR CODE STARTS HERE #
        cond = random.choice(['W', 'L'])
        if cond == 'W':
            self.experience += 5000
            return self.username + ' played a game. You won! You have gained 5000 experience points.'
        elif cond == 'L':
            self.experience += 3000
            return self.username + ' played a game. You lost! You have gained 3000 experience points.'

    def play_several(self, games):
        # YOUR CODE STARTS HERE #
        return_str = ''
        for i in range(games):
            return_str += self.play() + '\n'
        return return_str[:-1]


class RegularPlayer(Player):
    def level_up(self):
        # YOUR CODE STARTS HERE #
        if self.experience >= (self.level + 1) * 10000:
            self.level = self.experience // 10000
            return 'Promoted to level ' + str(self.level)
        else:
            return 'Not enough experience!'


class PremiumPlayer(Player):
    def __init__(self, username, region):
        # YOUR CODE STARTS HERE #
        super().__init__(username, region)
        self.experience = 1000
        self.level = 0
        return
    
    def promote(self):
        # YOUR CODE STARTS HERE #
        if self.experience >= (self.level + 1) * 6000:
            while self.experience >= (self.level + 1) * 6000:
                self.level += 1
                self.experience += 1000
            return 'Promoted to level ' + str(self.level)
        else:
            return 'Not enough experience!'


# Question 2

def q2_doctests():
    """
    Doctests for the classes and methods in Question 2

    >>> h1 = Hero("Tracer", 150, 20, 30)
    >>> h1.name == "Tracer"
    True
    >>> h1.ammo == 30
    True

    >>> h2 = Hero("Soldier", 200, 30, 30)
    >>> h2.health == 200
    True
    >>> h2.maximum_health == 200
    True

    >>> h1.attack(h2)
    'Soldier received 20 damage, but survived!'
    >>> h2.health == 180
    True
    >>> h2.maximum_health == 200
    True
    >>> h1.ammo == 29
    True

    >>> h2.heal(h1, 30, False)
    'Tracer healed Soldier to 200 health!'
    >>> h2.health
    200
    >>> h1.health
    120

    >>> h2.attack(h1, 10)
    'Tracer was killed after receiving 300 amount of damage!'

    >>> h1.attack(h2, 10)
    "Your character is dead! Can\'t attack!"

    >>> t1 = Tank("Roadhog", 600, 40, 8, 30)
    >>> h2.attack(t1, 15)
    'Roadhog received 420 damage, but survived!'

    >>> m1 = Healer("Mercy", 200, 10, 15)
    >>> m1.heal(h1, 50)
    'Your character is now alive! Mercy healed Tracer to 25 health!'
    """


class Hero:
    """
    Implementation of the Hero class
    """

    def __init__(self, name, health, base_damage, ammo):
        # YOUR CODE STARTS HERE #
        self.name = name
        self.health = health
        self.base_damage = base_damage
        self.ammo = ammo
        self.maximum_ammo = ammo
        self.maximum_health = health
        return

    def attack(self, other_character, ammo_usage = 1):
        # YOUR CODE STARTS HERE #
        if self.health <= 0:
            self.health = 0 
            return "Your character is dead! Can't attack!"
        else:
            shield = 0 
            if type(other_character) == Tank:
                shield = other_character.shield
            damage = (self.base_damage * ammo_usage) - shield
            self.ammo -= 1
            if self.ammo == 0:
                self.ammo = self.maximum_ammo
            other_character.health -= damage
            if other_character.health <= 0:
                other_character.health = 0
                return other_character.name + ' was killed after receiving ' \
                + str(damage) + ' amount of damage!'
            else:
                return other_character.name + ' received ' + str(damage) + \
                ' damage, but survived!'
    
    def heal(self, other_character, heal_amount, yourself = True):
        # YOUR CODE STARTS HERE #
        if yourself == True:
            if self.health <= heal_amount:
                return "Not enough health! Can't heal!"
            if other_character.health == 0:
                return "Your character is dead! Can't heal!"
            else:
                other_character.health += heal_amount
                self.health -= heal_amount
                if other_character.health > other_character.maximum_health:
                    other_character.health = other_character.maximum_health
                return self.name + ' healed ' + other_character.name + ' to ' \
                + str(other_character.health) + ' health!'
        if yourself == False:
            if other_character.health <= heal_amount:
                return "Not enough health! Can't heal!"
            if self.health == 0:
                return "Your character is dead! Can't heal!"
            else:
                self.health += heal_amount
                other_character.health -= heal_amount
                if self.health > self.maximum_health:
                    self.health = self.maximum_health
                return other_character.name + ' healed ' + self.name + ' to ' \
                + str(self.health) + ' health!'
    

class Tank(Hero):
    """
    Implementation of Tank class, a sublcass of Hero
    """

    def __init__(self, name, health, base_damage, ammo, shield):
        # YOUR CODE STARTS HERE #
        super().__init__(name, health, base_damage, ammo)
        self.shield = shield
        return

class Healer(Hero):
    """
    Impelemntation of Healer class, a sublcass of Hero
    """
    def heal(self, other_character, heal_amount):
        # YOUR CODE STARTS HERE #
        if other_character.health <= 0:
            other_character.health = 0
            other_character.health += int(heal_amount / 2)
            return 'Your character is now alive! ' + self.name + ' healed ' + \
                other_character.name + ' to ' \
                + str(other_character.health) + ' health!'
        else:
            other_character.health += heal_amount
            if other_character.health > other_character.maximum_health:
                other_character.health = other_character.maximum_health
            return self.name + ' healed ' + other_character.name +  ' to ' + \
                str(other_character.health) + ' health!'
            
