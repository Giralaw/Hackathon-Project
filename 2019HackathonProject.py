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
    print("Enter the morse code equivalent of the letter, exit to exit\n\n\n\n")
    while 1==1:
        targetLetter = random.choice(letterList)
        targetMorse = codes[targetLetter]
        inputMorse = input("   " + targetLetter + "\n\n\n\n")
        if inputMorse == targetMorse:
            clearConsole()
            print("   Correct!\n\n\n\n")
            print(targetMorse)
        elif inputMorse == "exit":
            break
        else:
            clearConsole()
            print("Incorrect\n\n\n\n")
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

print("\n\n\n                     WELCOME TO\n\n")
print("  __  __    ____    _____     _____   ______     __    ___    __ ")
print(" |  \/  |  / __ \  |  __ \   / ____| |  ____|   /_ |  / _ \  /_ |")
print(" | \  / | | |  | | | |__) | | (___   | |__       | | | | | |  | |")
print(" | |\/| | | |  | | |  _  /   \___ \  |  __|      | | | | | |  | |")
print(" | |  | | | |__| | | | \ \   ____) | | |____     | | | |_| |  | |")
print(" |_|  |_|  \____/  |_|  \_\ |_____/  |______|    |_|  \___/   |_|\n\n")
print("A Cole Parks Creation (featuring contributions from Alex Skeldon)\n\n\n\n\n\n\n\n\n\n\n")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nwhat would you like to do today?\n\n\n")
whichProgram = input("Enter 1 for continuous letter practice\nEnter 2 for word practice\n")
clearConsole()

letterPractice()