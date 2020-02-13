from __future__ import print_function
import random
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