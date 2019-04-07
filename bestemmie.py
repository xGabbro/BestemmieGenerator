import random
import string

consonants = "bcdfghlmnpqrstvz"
vocals = "aeiou"
stranger = "jkwxy"

def core():


    print("Modalità di scrittura:")
    print("1.Sulla shell")
    print("2.In un file di testo")
    choose = input("Scelta --> ")
    print("")
    print("Inserire il numero di bestemmie da generare:")
    number = int(input("--> "))

    if (choose == "1"):
        for i in range(0, number):
            msg = "Dio " + wordGen()
            print(msg)    
    elif (choose == "2"):
        print("Attendi...")
        text = open("bestemmie.txt", "w")
        for i in range(0, number):
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
