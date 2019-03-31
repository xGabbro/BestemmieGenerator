import random
import string

consonants = "bcdfghlmnpqrstvz"
vocals = "aeiou"
stranger = "jkwxy"

def core():

    choose = input("1.shell 2.file")

    if (choose == "1"):
        for i in range(1, 101):
            msg = "Dio " + wordGen()
            print(msg)    
    elif (choose == "2"):
        print("Attendi...")
        text = open("bestemmie.txt", "w")
        for i in range(1, 10**4):
            msg = "Dio " + wordGen()
            text.write(msg + "\n")
        print("Go finì!")

def wordGen():
    _word = ""

    for i in range(0, random.randint(3, 12)):
        _x = random.randint(1, 25)
        _y = random.randint(1, 10000)
        
        if(len(_word) % 2 == 0):

            if(_x == 1000):
                _word += vocals[random.randint(0, len(vocals) - 1)] + " "
            else:
                _word += consonants[random.randint(0, len(consonants) - 1)]

        else:

            if(_x == 25):
                 _word += consonants[random.randint(0, len(consonants) - 1)] + " "
            else:
                _word += vocals[random.randint(0, len(vocals) - 1)]
    
    return _word.replace(" ", "")

core()
input()
