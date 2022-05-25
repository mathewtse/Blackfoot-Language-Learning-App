### functions from helper.py are called here in order to keep a clean main.py ###

import helper as h
import images
import time

file = open("translations.csv")

location = "town"

## Dictionaries ##

# dictionary for each location #
townTranslations = h.dictionaryGenerator(file, "town")
restaurantTranslations = h.dictionaryGenerator(file, "restaurant")
homeTranslations = h.dictionaryGenerator(file, "home")
familyTranslations = h.dictionaryGenerator(file, "family")
greetingsTranslations = h.dictionaryGenerator(file, "greetings")
timeTranslations = h.dictionaryGenerator(file, "time")
verbTranslations = h.dictionaryGenerator(file, "verbs")

# dictionary for the custom testing, which tests all 5 scenes #
hardTestTranslations = {
    **townTranslations,
    **restaurantTranslations,
    **homeTranslations,
    **familyTranslations,
    **greetingsTranslations
}

# dictionary for all of the given vocab words #
allTranslations = {
    **townTranslations,
    **restaurantTranslations,
    **homeTranslations,
    **familyTranslations,
    **greetingsTranslations,
    **timeTranslations,
    **verbTranslations
}


## Keep highest score of each location here ##
townRecord = 0
restaurantRecord = 0
homeRecord = 0
familyRecord = 0
greetingsRecord = 0
hardTestRecord = 0

## called in main.py to start the game and show the image of the town ##
def firstImg():
    images.townImg()

## passes in different dictionaries depending on where the user is ##
def learn():
    if location == "town":
        h.learn(townTranslations)
    elif location == "restaurant":
        h.learn(restaurantTranslations)
    elif location == "home":
        h.learn(homeTranslations)
    elif location == "family":
        h.learn(familyTranslations)
    elif location == "greetings":
        h.learn(greetingsTranslations)


## calls the move() function defined in helper.py ##
def moveTo():
    # Refer to global location (variable on top) #
    global location
    location = h.move() 

## calls the test() function defined in helper.py ##
def basicTest():
    # updates the variables functionCaller.py #
    global townRecord
    global restaurantRecord
    global homeRecord
    global familyRecord
    global greetingsRecord
    global hardTestRecord

    if location == "town":
        townScore = h.test(townTranslations)
        if townScore > townRecord:
            townRecord = townScore
    elif location == "restaurant":
        restaurantScore = h.test(restaurantTranslations)
        if restaurantScore > restaurantRecord:
            restaurantRecord = restaurantScore
    elif location == "home":
        homeScore = h.test(homeTranslations)
        if homeScore > homeRecord:
            homeRecord = homeScore
    elif location == "family":
        familyScore = h.test(familyTranslations)
        if familyScore > familyRecord:
            familyRecord = familyScore
    elif location == "greetings":
        greetingsScore = h.test(greetingsTranslations)
        if greetingsScore > greetingsRecord:
            greetingsRecord = greetingsScore


## calls the test() function defined in helper.py ##
def hardTest():
    global hardTestRecord
    input(
        "In the hard test, the vocabulary from all 5 locations will be tested. <press enter to continue> "
    )
    hardTestScore = h.test(hardTestTranslations)
    if hardTestScore > hardTestRecord:
        hardTestRecord = hardTestScore

## this functions shows the highest scores of each location##
def showScores():
    print()
    print("Highest test scores:")
    print("Town: " + str(townRecord))
    print("Restaurant: " + str(restaurantRecord))
    print("Home: " + str(homeRecord))
    print("Family: " + str(familyRecord))
    print("Greetings: " + str(greetingsRecord))
    print("Hard Test: " + str(hardTestRecord))
    time.sleep(4)

## creating a new function called speech() that is to be called in main.py ##
## Enables the speech synthesis feature ##
def speech():
    h.speechSynthesis(allTranslations)


