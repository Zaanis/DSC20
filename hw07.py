"""
DSC 20 Fall 2022 Homework 07
Name: Joshua Chen   
PID: A16810747
"""
## RECURSION SECTION ##

# Question 1
def multiply(chars, nums):
    """
    ##############################################################
    create output string based on character list passed in
    output string should be palindrome
    if number is odd, add corresponding character n times to both
    beginning and end
    if number is even, add corresponding character n times evenly to
    beginning and end
    ##############################################################

    >>> multiply(["a", "b", "c"], [1, 2, 3])
    'abccccccba'
    >>> multiply(["e", "l", "k", "p"], [1, 0, 1, 2])
    'ekppke'
    >>> multiply(["b"], [8])
    'bbbbbbbb'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> multiply(['a'], [1])
    'aa'
    >>> multiply(['a'], [0])
    ''
    >>> multiply(['a', 'b'], [5, 4])
    'aaaaabbbbaaaaa'
    """
    # YOUR CODE GOES HERE #
    double = 2
    if len(chars) == 0:
        return ''
    if nums[0] % double == 1:
        return chars[0] * nums[0] + multiply(chars[1:], nums[1:]) + \
        chars[0] * nums[0]
    else:
        return  chars[0] * (nums[0] // double) + \
        multiply(chars[1:], nums[1:]) + chars[0] * (nums[0] // double)
    

# Question 2
def maze(coord, map):
    """
    Given 'coord' as a tuple and 'map' as list of strings,
    return 'treasure!' if treasure can be reached by following the signs
    return 'sad' otherwise
    There is no cycle
    >>> map = [
    ... "..............",
    ... ".RRRD..RRRRD..",
    ... "...DL..U...D..",
    ... "...D...U.D.D..",
    ... "...RRRRU.D.*..",
    ... ".............."]
    >>> maze((1,1), map)
    'treasure!'
    >>> maze((0,0), map)
    'sad'
    >>> maze((3,9), map)
    'sad'
    >>> maze((4,11), map)
    'treasure!'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> maze((5,11), map)
    'sad'
    >>> maze((4,11), map)
    'treasure!'
    >>> maze((4, 3), map)
    'treasure!'
    """
    # YOUR CODE GOES HERE #
    x_coord = coord[0]
    y_coord = coord[1]
    if map[x_coord][y_coord] == "*":
        return 'treasure!'
    elif map[x_coord][y_coord] == ".":
        return 'sad'
    elif map[x_coord][y_coord] == "R":
        y_coord += 1
        return maze((x_coord, y_coord), map)
    elif map[x_coord][y_coord] == "L":
        y_coord -= 1
        return maze((x_coord, y_coord), map)
    elif map[x_coord][y_coord] == "U":
        x_coord -= 1
        return maze((x_coord, y_coord), map)
    elif map[x_coord][y_coord] == "D":
        x_coord += 1
        return maze((x_coord, y_coord), map)


# Question 3
def count_substring(s, first, last):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> count_substring("a", "a", "b")
    0
    >>> count_substring("abcab", "a", "b")
    3
    >>> count_substring("aaaa", "a", "a")
    10

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> count_substring('ab','a','a')
    1
    >>> count_substring('aba', 'a', 'c')
    0
    >>> count_substring('abcdefggfedcba', 'c', 'd')
    2
    """
    # YOUR CODE GOES HERE #
    if len(s) == 0:
        return 0
    elif len(s) == 1 and first == last and first == s:
        return 1
    elif len(s) == 1 and first != last:
        return 0
    elif s[0] == first and s[-1] == last:
        return 1 + count_substring(s[1:], first, last) + \
        count_substring(s[:-1], first, last) - \
        count_substring(s[1:-1], first, last)
    elif s[0] != first or s[-1] != last:
        return 0 + count_substring(s[1:], first, last) + \
        count_substring(s[:-1], first, last) - \
        count_substring(s[1:-1], first, last)


# Question 4: Extra Credit
def lutee_reproduction(months):
    """
    >>> lutee_reproduction(1)
    2
    >>> lutee_reproduction(2)
    2
    >>> lutee_reproduction(3)
    4
    >>> lutee_reproduction(4)
    6
    >>> lutee_reproduction(6)
    16
    """
    if months == 1:       
        starting_value = 2
        return starting_value
    if months == 0:
        return 0
    else:
        previous_months = 2
        return lutee_reproduction(months - 1) + \
        lutee_reproduction(months - previous_months)

## OOP SECTION ##
def doctests_go_here():
    """
    >>> website1 = Website('Google', 'google.com', True, 500, ['Chrome', \
'Safari', 'Firefox', 'Edge'])
    >>> print(website1)
    Google linked at google.com is available on ['Chrome', 'Safari', \
'Firefox', 'Edge'] platforms. It's been interacted with 500 times already!
    >>> website1.get_name()
    'Google'
    >>> Website.server
    'DNS'
    >>> website1.server
    'DNS'
    >>> browser1 = Browser('Chrome', 'Karina')
    >>> print(browser1)
    Browser Chrome opened by Karina has 0 tabs open.
    >>> browser1.open_tab(website1)
    True
    >>> browser1.get_num_tabs()
    1
    >>> print(browser1)
    Browser Chrome opened by Karina has 1 tabs open.
    >>> browser1.open_tab(website1)
    True
    >>> browser1.close_tab(website1)
    True

    >>> website2 = Website('Canvas', 'canvas.ucsd.edu', False, 10, ['Chrome', \
'Safari'])
    >>> website3 = Website('Gradescope', 'gradescope.com', False, 100, \
['Chrome', 'Firefox'])
    >>> browser1.open_tab(website2)
    True
    >>> website3.add_to_browser(browser1)
    True
    >>> print(browser1.interact_all())
    Karina Clicked on Google at google.com
    Karina Clicked on Canvas at canvas.ucsd.edu
    Karina Clicked on Gradescope at gradescope.com
    >>> browser1.get_total_clicks()
    613
    >>> browser2 = Browser('Safari', 'Ben')
    >>> browser2.open_tab(website1)
    True
    >>> website2.add_to_browser(browser2)
    True
    >>> browser2.open_tab(website3)
    False
    >>> print(browser2)
    Browser Safari opened by Ben has 2 tabs open.
    >>> [website.get_name() for website in browser2.get_history()]
    ['Google', 'Canvas']
    >>> browser2.combine_windows(browser1)
    2
    >>> [website.get_name() for website in browser2.get_websites()]
    ['Google', 'Canvas', 'Google', 'Canvas']
    >>> browser2.get_num_tabs()
    4
    >>> browser2.clear_history(3)
    True
    >>> [website.get_name() for website in browser2.get_history()]
    ['Canvas']
    >>> website1.refresh()
    'refreshed!'
    >>> website1.get_num_clicks()
    0
    
    #WEBSITE CONSTRUCTOR DOCTEST
    >>> w3 = Website('Youtube', 'youtube.com', True, 100, \
    ['Chrome', 'Edge', 'Safari', 'IE'])
    >>> w4 = Website('yahoo', 'yahoo.com', False, 100, \
    ['Opera', 'IE'])
    >>> w5 = Website('Gmail', 'mail.google.com', False, 100, \
    ['Chrome', 'Edge']) 
    >>> w3.name
    'Youtube'
    >>> w4.name
    'yahoo'
    >>> w5.name
    'Gmail'
    >>> w3.url
    'youtube.com'
    >>> w4.url
    'yahoo.com'
    >>> w5.url
    'mail.google.com'
    >>> w3.has_audio
    True
    >>> w4.has_audio
    False
    >>> w5.has_audio
    False
    >>> w3.num_clicks
    100
    >>> w4.num_clicks
    100
    >>> w5.num_clicks
    100
    >>> w3.browser_compatibility
    ['Chrome', 'Edge', 'Safari', 'IE']
    >>> w4.browser_compatibility
    ['Opera', 'IE']
    >>> w5.browser_compatibility
    ['Chrome', 'Edge']
    >>> w3.get_name()
    'Youtube'
    >>> w4.get_name()
    'yahoo'
    >>> w5.get_name()
    'Gmail'
    >>> w3.get_url()
    'youtube.com'
    >>> w4.get_url()
    'yahoo.com'
    >>> w5.get_url()
    'mail.google.com'
    >>> w3.get_has_audio()
    True
    >>> w4.get_has_audio()
    False
    >>> w5.get_has_audio()
    False
    >>> w3.get_num_clicks()
    100
    >>> w4.get_num_clicks()
    100
    >>> w5.get_num_clicks()
    100
    >>> w3.get_browser_compatibility()
    ['Chrome', 'Edge', 'Safari', 'IE']
    >>> w4.get_browser_compatibility()
    ['Opera', 'IE']
    >>> w5.get_browser_compatibility()
    ['Chrome', 'Edge']
    >>> print(w3)
    Youtube linked at youtube.com is available on ['Chrome', 'Edge',\
 'Safari', 'IE'] platforms. It's been interacted with 100 times already!
    >>> print(w4)
    yahoo linked at yahoo.com is available on ['Opera', 'IE'] platforms.\
 It's been interacted with 100 times already!
    >>> print(w5)
    Gmail linked at mail.google.com is available on ['Chrome', 'Edge']\
 platforms. It's been interacted with 100 times already!
    
    #BROWSER CONSRUCTOR DOCTEST
    >>> b3 = Browser('IE', 'A') 
    >>> b4 = Browser('Opera', 'B')
    >>> b5 = Browser('Edge', 'C')
    >>> b3.name
    'IE'
    >>> b4.name
    'Opera'
    >>> b5.name
    'Edge'
    >>> b3.user
    'A'
    >>> b4.user
    'B'
    >>> b5.user
    'C'
    >>> b3.num_tabs
    0
    >>> b4.num_tabs
    0
    >>> b5.num_tabs
    0
    >>> b3.websites
    []
    >>> b4.websites
    []
    >>> b5.websites
    []
    >>> b3.history
    []
    >>> b4.history
    []
    >>> b5.history
    []
    >>> b3.get_name()
    'IE'
    >>> b4.get_name()
    'Opera'
    >>> b5.get_name()
    'Edge'
    >>> b3.get_user()
    'A'
    >>> b4.get_user()
    'B'
    >>> b5.get_user()
    'C'
    >>> b3.get_num_tabs()
    0
    >>> b4.get_num_tabs()
    0
    >>> b5.get_num_tabs()
    0
    >>> b3.get_websites()
    []
    >>> b4.get_websites()
    []
    >>> b5.get_websites()
    []
    >>> b3.get_history()
    []
    >>> b4.get_history()
    []
    >>> b5.get_history()
    []
    >>> print(b3)
    Browser IE opened by A has 0 tabs open.
    >>> print(b4)
    Browser Opera opened by B has 0 tabs open.
    >>> print(b5)
    Browser Edge opened by C has 0 tabs open.

    #WEBSITE CLICK METHOD DOCTEST
    >>> w3.click('A')
    'A interacted with Youtube at youtube.com'
    >>> w4.click('B')
    'B interacted with yahoo at yahoo.com'
    >>> w5.click('C')
    'C interacted with Gmail at mail.google.com'
    
    #WEBSITE ADD TO BROWSER DOCTEST
    >>> w3.add_to_browser(b3)
    True
    >>> w3.add_to_browser(b4)
    False
    >>> w3.add_to_browser(b5)
    True
    
    #WEBSITE CHECK BROWSER COMPATIBILITY DOCTEST
    >>> w3.check_browser_compatibility(b3)
    True
    >>> w3.check_browser_compatibility(b4)
    False
    >>> w3.check_browser_compatibility(b5)
    True

    #WEBSITE PLAY AUDIO DOCTEST
    >>> w3.play_audio()
    'doo da do!'
    >>> w4.play_audio()
    'no audio.'
    >>> w5.play_audio()
    'no audio.'
    
    #BROWSER OPEN TAB DOCTEST
    >>> b3.open_tab(w5)
    False
    >>> b4.open_tab(w4)
    True
    >>> b5.open_tab(w3)
    True
    
    #BROWSER CLOSE TAB DOCTEST
    >>> b3.close_tab(w5)
    False
    >>> b4.close_tab(w4)
    True
    >>> b5.close_tab(w3)
    True

    #BROWSER CLEAR HISTORY DOCTEST
    >>> b3.clear_history(10)
    False
    >>> b4.clear_history(1)
    True
    >>> b4.clear_history(3)
    False

    #BROWSER GET TOTAL CLICKS DOCTEST
    >>> b3.get_total_clicks()
    101
    >>> b4.get_total_clicks()
    0
    >>> b5.get_total_clicks()
    101
    
    #BROWSER INTERACT ALL DOCTEST
    >>> b3.interact_all()
    'A Clicked on Youtube at youtube.com'
    >>> b4.interact_all()
    'Empty'
    >>> b5.interact_all()
    'C Clicked on Youtube at youtube.com'
    
    #BROWSER COMBINE WINDOWS DOCTEST
    >>> b3.combine_windows(b4)
    True
    >>> b4.combine_windows(b3)
    0
    >>> b5.combine_windows(b3)
    True
    
    #WEBSITE REFRESH DOCTEST
    >>> w3.refresh()
    'refreshed!'
    >>> w4.refresh()
    'refreshed!'
    >>> w5.refresh()
    'refreshed!'
    >>> w3.get_num_clicks()
    0
    >>> w4.get_num_clicks()
    0
    >>> w5.get_num_clicks()
    0
    """
    return

class Website:
    """
    Implementation of a website
    """

    server = "DNS"

    def __init__(self, name, url, has_audio, num_clicks, \
    browser_compatibility):
        """
        ##############################################################
        name is given by constructor's argument, indicate name of website,
        passed in as str
        url given by argument, indicate address of website, passed in as str
        has_audio given by argument, indicates whether the website has audio,
        passed in as boolean
        num_clicks given by argument, indicates number of 'click' occured,
        passed in as integer
        browser_compatibility given by argument, indicates browsers this 
        website can run on, given in a list
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        assert type(name) == str and len(name) != 0
        assert type(url) == str and len(url) != 0
        two = 2
        assert len(url.split('.')) >= two and \
        len(url.split('.')[len(url.split('.')) - 1]) >= two
        assert type(has_audio) == bool
        assert type(num_clicks) == int
        assert type(browser_compatibility) == list
        self.name = name
        self.url = url
        self.has_audio = has_audio
        self.num_clicks = num_clicks
        self.browser_compatibility = browser_compatibility

    def get_name(self):
        """ Getter for name attribute """
        # YOUR CODE GOES HERE #
        return self.name

    def get_url(self):
        """ Getter for url attribute """
        # YOUR CODE GOES HERE #
        return self.url

    def get_has_audio(self):
        """ Getter for the has_audio attribute """
        # YOUR CODE GOES HERE #
        return self.has_audio

    def get_num_clicks(self):
        """ Getter for num_clicks attribute """
        # YOUR CODE GOES HERE #
        return self.num_clicks

    def get_browser_compatibility(self):
        """ Getter for browser_compatibility attribute """
        # YOUR CODE GOES HERE #
        return self.browser_compatibility

    def __str__(self):
        """ String representation of Website """
        # YOUR CODE GOES HERE #
        return self.get_name() + ' linked at ' +  self.get_url() + ' is \
available on ' + str(self.get_browser_compatibility()) + " \
platforms. It's been interacted with " + str(self.get_num_clicks \
        ()) + ' times already!'

    def click(self, user):
        """
        ##############################################################
        return string with format x interacted with y at z
        increase num_click by 1
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        self.num_clicks += 1
        return user + ' interacted with ' + self.get_name() + ' at ' + \
            self.get_url()

    def add_to_browser(self, browser):
        """
        ##############################################################
        add website to given Broswer instance. Return True if successful
        return False otherwise
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        assert type(browser) == Browser
        if browser.open_tab(self):
            return True
        else:
            return False

    def check_browser_compatibility(self, browser):
        """
        ##############################################################
        checks whether an associated browser is compatible with website
        return True if yes else False
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        if browser.get_name() in self.get_browser_compatibility():
            return True
        else:
            return False

    def refresh(self):
        """
        ##############################################################
        clears click history of website
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        self.num_clicks = 0
        return 'refreshed!'

    def play_audio(self):
        """
        ##############################################################
        attemps to play associated audio, return 'doo da doo!' if there is
        audio, else return 'no audio.'
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        if self.get_has_audio() == True:
            return 'doo da do!'
        else:
            return 'no audio.'

        
class Browser:
    """
    Implementation of a browser
    """

    def __init__(self, name, user):
        """
        ##############################################################
        instace attributes of browser
        name given by argument, indicate name of browser, given as str
        user given by argument, indicate name of user, given as str
        num_tabs not provided, track active tabs, given as int
        history not provided, track history, list of Website objects
        websites not provided, list of Website objects
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        assert type(name) == str and len(name) > 0
        assert type(user) == str and len(user) > 0
        self.name = name
        self.user = user
        self.num_tabs = 0
        self.websites = []
        self.history = []

    def get_name(self):
        """ Getter for name attribute """
        # YOUR CODE GOES HERE #
        return self.name

    def get_user(self):
        """ Getter for user attribute """
        # YOUR CODE GOES HERE #
        return self.user

    def get_num_tabs(self):
        """ Getter for num_tabs attribute """
        # YOUR CODE GOES HERE #
        return self.num_tabs

    def get_history(self):
        """ Getter for history attribute """
        # YOUR CODE GOES HERE #
        return self.history

    def get_websites(self):
        """ Getter for websites attribute """
        # YOUR CODE GOES HERE #
        return self.websites

    def __str__(self):
        """ String representation of Browser """
        # YOUR CODE GOES HERE #
        return 'Browser ' + self.get_name() + ' opened by ' + self.get_user() + ' has ' + str(self.get_num_tabs()) + ' tabs open.'

    def open_tab(self, website):
        """
        ##############################################################
        add website to browser, if able to, do it and return True
        else return False
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        assert type(website) == Website
        if self.get_name() in website.get_browser_compatibility():
            self.num_tabs += 1
            self.websites += [website]
            self.history += [website]
            return True
        else:
            return False

    def close_tab(self, website):
        """
        ##############################################################
        remove website from browser, if successful, return True,
        else, return False
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        assert type(website) == Website
        if website in self.get_websites():
            self.num_tabs = self.num_tabs - 1
            if len(self.websites) == 1:
                self.websites = []
            else:
                self.get_websites().remove(website)
            return True
        else:
            return False

    def clear_history(self, n):
        """
        ##############################################################
        remove first n items in browser history. If n is larger than items in 
        history, return False, otherwise return True and perform action
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        assert n > 0
        if n > len(self.get_history()):
            return False
        else:
            for i in range(n):
                self.get_history().pop(0)
            return True

    def get_total_clicks(self):
        """
        ##############################################################
        return total amount of clicks of websites in browser
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        return sum([web.get_num_clicks() for web in self.get_websites()])

    def interact_all(self):
        """
        ##############################################################
        click on every website in browser once. return string containing
        information on all websites interacted with,
        if browser is empty, return empty.
        return string in format:
        (user) clicked on (website) at (url)
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        if len(self.get_websites()) > 0:
            return_str = ''
            for web in self.get_websites():
                return_str += web.click(self.user) + '\n'
            return_str2 = return_str.replace('interacted with', 'Clicked on')
            return return_str2[:-1]
        else:
            return 'Empty'
    def combine_windows(self, other_browser):
        """
        ##############################################################
        add all website from other browser to this browser, if all websites
        added successfully, return True, else return number of websites added
        ##############################################################
        """
        # YOUR CODE GOES HERE #
        assert type(other_browser) == Browser
        to_add = [x for x in other_browser.get_websites() \
        if x.check_browser_compatibility(self)]
        self.num_tabs += len(to_add)
        self.history += to_add
        self.websites += to_add
        if len(to_add) == len(other_browser.get_websites()):
            return True
        else:
            return len(to_add)