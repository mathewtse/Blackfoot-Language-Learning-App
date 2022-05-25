## Most of my functions are defined here ## 
## They are called in functionCaller.py ##
# CMPT 120
# Nov. 12, 2020

import wave
import time
import random
import images
from replit import audio
import replit
import functionCaller as f


## Dictionary Generator Function ##
## Returns a certain number of lines - depends on the location parameter ##

def dictionaryGenerator(csvFile, location):

    if location == "town":
        vocabWords = 6
    elif location == "restaurant":
        vocabWords = 10
    elif location == "home":
        vocabWords = 7
    elif location == "family":
        vocabWords = 6
    elif location == "greetings":
        vocabWords = 8
    elif location == "time":
        vocabWords = 3
    elif location == "verbs":
        vocabWords = 2

    dictionaryTemp = {}

    # reads each line of the CSV file and creates a dictionary #
    for x in range(vocabWords):
        currentLine = csvFile.readline()
        currentLineModified = currentLine.strip().split(",")
        dictionaryTemp[(currentLineModified[0]).lower().strip()] = (
            currentLineModified[1]).lower().strip()

    return dictionaryTemp


## End of dictionary function ##




## Function to move between scenes ##


def move():
    location = input(
        "Where do you want to go (Town/Restaurant/Home/Family/Greetings)? "
    ).lower().strip().strip("!.,")
    if location == "town":
        # show image of town
        images.townImg()
        replit.clear()
        return "town"
    elif location == "restaurant":
        images.restaurantImg()
        replit.clear()
        return "restaurant"
    elif location == "home":
        images.homeImg()
        replit.clear()
        return "home"
    elif location == "family":
        images.familyImg()
        replit.clear()
        return "family"
    elif location == "greetings":
        images.greetingsImg()
        replit.clear()
        return "greetings"


## End of move function ##




## Sound function ##

def sound(english):
    try:    
        # modify the english word to make it the same as the files - underscore instead of spaces, etc etc
        englishEdited = english.replace(" ", "_").replace("'","").strip("?.").replace(".","")
        source = audio.play_file("sounds/" + englishEdited + ".wav")
        source.paused = not source.paused
    except:
        print("currently unable to play audio due to replit bugs")
        
## End of sound function ##




## Learn function ##


def learn(locationsDictionary):
    replit.clear()
    wantToLearn = True
    print(
        "Great! let's Learn! Look around here and tell me a word in English.")
    while wantToLearn:
        blackFootWord = input(
            "What Blackfoot word do you want to learn?\nType it in English, or type done to finish. "
        ).strip().strip("!,.").lower()
        if blackFootWord != "done" and blackFootWord in locationsDictionary:
            print(locationsDictionary[blackFootWord])
            sound(blackFootWord)  # sound function for audio
            time.sleep(2) ## allow the user to see the translation for 2 secs
            replit.clear()
        elif blackFootWord == "done":
            wantToLearn = False
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
            replit.clear()


## End of learn function ##




## Test function ##


def test(trans):
    points = 0

    for x in range(10):
        replit.clear()
        currentWord = random.choice(list(trans)) # choose english word from dictionary
        sound(currentWord)  ## SOUND
        '''
        change the selected English word to Blackfoot,
        and ask the user what that word is
        ''' 
        inputtedWord = input("What is " + trans[currentWord] + "? ").lower() 
        if inputtedWord == currentWord:
            print("Good job!")
            time.sleep(2)
            points += 1
            replit.clear()
        else:
            print("Nope, it's " + currentWord)
            time.sleep(2)
            replit.clear()

    input("You got " + str(points) + " right! Press <enter>")
    replit.clear()
    return points


## End of test function ##




## Concat Function ##


def concat(infiles, outfile):
    """
  Input:
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
    data = []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()


## End of concat function ##




## Speech synthesis ##


def speechSynthesis(allTranslations):
  replit.clear()
  # while loop to continue speech synthesis until user says no #
  continueSpeechSynthesis = True
  while continueSpeechSynthesis:
    # create the keys for each dictionary #
    townKeys = list(f.townTranslations.keys())
    restaurantKeys = list(f.restaurantTranslations.keys())
    homeKeys = list(f.homeTranslations.keys())
    timeKeys = list(f.timeTranslations.keys())
    verbKeys = list(f.verbTranslations.keys())

    # welcome the user #
    print("Welcome to the speech synthesis feature!")
    time.sleep(2)
    input(
        "\nHere, you will construct an English sentence, and we will teach you the Blackfoot translation!\n<Press enter to continue>\n "
    )
    replit.clear()

    # Take user input for time words #
    correctTime = False
    while not correctTime:
        # print timeKeys without the quotiation marks #
        print('[%s]' % ', '.join(map(str, timeKeys)))
        timeWord = input(
            "Please type in one of the options from above list --> ").lower()
        if timeWord in timeKeys:
            correctTime = True
            timeWordBlack = allTranslations[timeWord]
            print()

    # Take user input for verb words #
    correctVerb = False
    while not correctVerb:
        # print verbKeys without the quotiation marks #
        print('[%s]' % ', '.join(map(str, verbKeys)))
        verbWord = input(
            "Please type in one of the options from above list --> ").lower()
        if verbWord in verbKeys:
            correctVerb = True
            verbWordBlack = allTranslations[verbWord]
            print()

    # Take user input for third word #
    correctThirdWord = False
    while not correctThirdWord:
        if verbWord == "i will go":
            # print townKeys and homeKeys without quotation marks #
            print('[%s]' % ', '.join(map(str, townKeys)))
            print('[%s]' % ', '.join(map(str, homeKeys)))
            thirdWord = input(
                "Please type in one of the options from the above lists --> "
            ).lower()
            if thirdWord in townKeys or thirdWord in homeKeys:
                correctThirdWord = True
                thirdWordBlack = allTranslations[thirdWord]
                print()

        elif verbWord == "i will eat":
            # print restaurantKeys without quotation marks #
            print('[%s]' % ', '.join(map(str, restaurantKeys)))
            thirdWord = input(
                "Please type in one of the options from above --> ").lower()
            if thirdWord in restaurantKeys:
                correctThirdWord = True
                thirdWordBlack = allTranslations[thirdWord]
                print()

    print(timeWord + " " + verbWord + " " + thirdWord)
    print(timeWordBlack + " " + verbWordBlack + " " + thirdWordBlack)

    # combine the .wav files in preparation to use the concat function #
    soundIn = [("sounds/" + timeWord.replace(" ", "_") + ".wav"),
               ("sounds/" + verbWord.replace(" ", "_") + ".wav"),
               ("sounds/" + thirdWord + ".wav")]

    concat(soundIn, "sounds/soundOut.wav")
    sound("soundOut")
    time.sleep(2)
    
    continueOrNot = input("Do you want to continue speech synthesis? Yes or No? --> ").lower().strip()
    if continueOrNot == "yes":
      continueSpeechSynthesis = True
    elif continueOrNot == "no":
      continueSpeechSynthesis = False
    else: 
      print("Sorry I don't understand. I will assume that you don't want to continue.")
      continueSpeechSynthesis = False


## End of speech synthesis function ##


