# @author iedgeley
# @date 7.23.14
# @title Simple guessing game in two versions - with a loop and recursively.

import random

def goguess():
    rand = random.randint(1,21)
    print "I have a number between 1 and 20 inclusive."
    guess = 0
    while(guess!= rand):
        try:
            guess = int(raw_input("Guess: "))
        except:
            print "Error"
        if guess < rand:
            print "Guess is too low!"
        elif guess > rand:
            print "Guess is too high!"
        else:
            print "Well done!"

def goguessrecur(r):
    g = ""
    try:
        g = int(raw_input("Guess: "))
    except:
        print "Error"
    if g == r:
        print "Well done!"
    elif g < r:
        print "Too low!"
        goguessrecur(r)
    else:
        print "Too high!"
        goguessrecur(r)

goguessrecur(random.randint(1,21))