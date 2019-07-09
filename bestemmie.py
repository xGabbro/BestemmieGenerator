import random
import string

consonants = ""
stranger = ""
vocals = ""

consonantsDict = { "b" : 2, "c": 9, "d" : 8, 
                    "f" : 2, "g": 3, "h" : 3, 
                    "l" : 13, "m": 5, "n" : 14, 
                    "p" : 6, "q": 1, "r" : 13, 
                    "s" : 10, "t": 11, "v" : 4, 
                    "z" : 1 }

strangerDict = { "j" : 1, "k": 1, "w" : 1,
                "x" : 3, "y": 1}

vocalsDict = { "a" : 12, "e": 12, "i" : 11, 
                "o" : 10, "u": 3 }

def core():

    strInit()

    print("Modalità di scrittura:")
    print("1.Sulla shell")
    print("2.In un file di testo")

    choose = input("Scelta --> ") 

    print("")
    print("Inserire il numero di bestemmie da generare:")
    number = int(input("--> "))

    if (choose == "1"):
        onShell(number)
    elif (choose == "2"):
        print("Attendi...")
        text = open("bestemmie.txt", "w")
        for i in range(0, number):
            msg = "Dio " + wordGen()
            text.write(msg + "\n")
        print("Go finì!")
    else:
        print("Errore! Scegliere un opzione valida!")
        clearMyButt()
        core()

def onShell(number):
    bestemmieList = []

    if (number > 100):
        input("Errore! Capisco che ti piacciono le bestemmie, ma ne puoi generare massimo 100 alla volta sulla shell")
        clearMyButt()
        core()

    for i in range(0, number):
            msg = "Dio " + wordGen()
            bestemmieList.append(msg)
            print(str(i).zfill(2) + "   --->   " + msg)
    
    bestemmieFile = open("bEST_Bestemmie.txt", "a")

    print("\n" + "Scegli le bestemmie che vuoi salvare separate da una virgola")
    dirtyValues = input("Valori ---> ").split(",")

    clearValues = []

    for i in dirtyValues:
        clearValues.append(int(i))

    for i in clearValues:
        bestemmieFile.write(bestemmieList[i] + "\n")

def strInit():

    global stranger
    global vocals
    global consonants

    for _char in consonantsDict:
        for i in range(0, consonantsDict[_char]):
            consonants += _char

    for _char in vocalsDict:
        for i in range(0, vocalsDict[_char]):
            vocals += _char
    
    for _char in strangerDict:
        for i in range(0, strangerDict[_char]):
            stranger += _char

def wordGen():
    doubleConsonantValue = 30
    doubleVocalValue = 60
    strangerConsonantValue = 100
    doubleBanned = "hjqwy"

    _latch = ""

    _word = ""

    _wordLen = random.randint(3, 12)
    for i in range(0, _wordLen):
        a = random.randint(1, doubleConsonantValue)
        b = random.randint(1, doubleVocalValue)
        c = random.randint(1, strangerConsonantValue)
        
        if(len(_word) % 2 == 0):

            if(b == int(doubleVocalValue / 2)):

                _word += vocals[random.randint(0, len(vocals) - 1)] + " "

            else:

                if (c == int(strangerConsonantValue / 2)):
                    _latch = stranger[random.randint(0, len(stranger) - 1)]
                else:
                    _latch = consonants[random.randint(0, len(consonants) - 1)]
                
                _word += _latch

        else:

            if(a == int(doubleConsonantValue / 2) and i != 1 and i != _wordLen - 1 and _latch not in doubleBanned):

                #_word += consonants[random.randint(0, len(consonants) - 1)] + " "
                _word += _latch + " "

            else:

                _word += vocals[random.randint(0, len(vocals) - 1)]
                _latch = ""
    
    return _word.replace(" ", "")

def clearMyButt():
    for i in range(0, 10):
        print("")

core()
input()
