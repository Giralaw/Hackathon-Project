import random
import time

codes = {


"a" : ".-",
"b" : "-...",
"c" : "-.-.",
"d" : "-..",
"e" : ".",
"f" : "..-.",
"g" : "--.",
"h" : "....",
"i" : "..",
"j" : ".---",
"k" : "-.-",
"l" : ".-..",
"m" : "--",
"n" : "-.",
"o" : "---",
"p" : ".--.",
"q" : "--.-",
"r" : ".-.",
"s" : "...",
"t" : "-",
"u" : "..-",
"v" : "...-",
"w" : ".--",
"x" : "-..-",
"y" : "-.--",
"z" : "--..",

"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
}

#
#
#

morseLetter = ""
letter = "e"
targetLetter = ""
targetMorse = ""
inputLetter = ""
inputMorse = ""

letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#
#
#

def clearConsole():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def letterPractice():
    print("Enter the morse code equivalent of these letters, exit to exit\n")
    while 1==1:
        targetLetter = random.choice(letterList)
        targetMorse = codes[targetLetter]
        inputLetter = input(targetLetter + "\n")
        if inputMorse == targetMorse:
            print("Correct!\n")
        elif inputMorse == "exit":
            break
        else:
            print("Incorrect\n")
        #random letter generator
    #checks if user input is correct

def convertletter(let):
    if len(let)>1:
        print("Please give a single letter")
    else:
        targetLetter = codes[let]

#
#
#

whichProgram = input("Enter 1 for continuous letter practice\nEnter 2 for word practice\n")
clearConsole()

letterPractice()