# Mathew Tse
# CMPT 120 Blackfoot Project
# this file consists of the main loop which allows the user to navigate
# through the different features of the app

import functionCaller as f
import replit

# show image of town
f.firstImg()

run = True

while run:
    replit.clear()
    operation = input(
        "Do you want to learn some words around you (learn),\nhave me test you (test), have me test you on all locations (hardTest),\nhave me translate english sentences to blackfoot for you (speech)\ngo somewhere else (move) check your scores (scores) or leave (exit)? "
    ).lower().strip().strip(".,!")

    if operation == "learn":
        f.learn()
    elif operation == "move":
        f.moveTo()
    elif operation == "test":
        f.basicTest()
    elif operation == "hard test" or operation == "hardtest":
        f.hardTest()
    elif operation == "speech synthesis" or operation == "speech":
        f.speech()
    elif operation == "scores" or operation == "score":
        f.showScores()
    elif operation == "exit":
        run = False
    else:
        print("Sorry, I don't understand. Please try again.")
