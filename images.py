# all my functions for showing images of the 5 scenes #
# these functions are called in the move() function in helper.py #
# townImg() called once in functionCaller.py #

import cmpt120image as c

def townImg():
    townImg = c.getImage("images/town.jpg")
    c.showImage(townImg,"Town")

def restaurantImg():
    restaurantImg = c.getImage("images/restaurant.jpg")
    c.showImage(restaurantImg,"Restaurant")

def homeImg():
    homeImg = c.getImage("images/home.jpg")
    c.showImage(homeImg,"Home")

def familyImg():
    familyImg = c.getImage("images/family.jpg")
    c.showImage(familyImg,"Family")

def greetingsImg():
    greetingsImg = c.getImage("images/greetings.jpg")
    c.showImage(greetingsImg,"Greetings")