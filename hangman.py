from __future__ import print_function
import random
lives = 6
word = ""
letter = ""
updatedSpaces = []
def initialize():
    global word
    global updatedSpaces
    word = "airport"
    print ("_ " * len(word))
    updatedSpaces = ("_ " * len(word))
    print("try to guess the word in less than 6 tries")
    print(updatedSpaces)
def getLetter():
    global letter
    print ("What is your guess")
    letter = raw_input()
#def check():        
def win():
    if updatedSpaces == word:
        print("you won the game!")
    else:
        if lives == 0:
            print("you lost")
def main():
    initialize()
    getLetter()
    #check()
lives = 6
words = "hello"
letter = " "
updatedspaces = ['_', '_', '_', '_', '_']
'''
def main():
    #initilze()
    getLetter()
    check()
    
def getLetter():
    global letter
    letter = str(input("type your guess here: "))
    check()
'''
def check():
    # checks the guess that the user makes
    global word
    global lives
    global updatedspaces
    if letter in words:
        i = (words.find(letter)) 
        del updatedspaces[i]
        updatedspaces.insert(i, letter)
        if i != len(words)-1:
            e = (words.find(letter, i+1, len(words) -1))
            if e != -1:
                del updatedspaces[e]
                updatedspaces.insert(e, letter)
                if e != len(words)-1:
                    a = words.find(letter, e+1, len(words)+1)
                    if a != -1:
                        del (updatedspaces[a])
                        updatedspaces.insert(a, letter)
                else:
                    won()
        else:
            won()
                
    if letter not in words:
        print ('Sorry this letter is not in word')
        lives -= 1
        print ('You have', lives, 'lives left')
        getLetter() 
    print (updatedspaces[0])
    print (updatedspaces)
    getLetter()
main()