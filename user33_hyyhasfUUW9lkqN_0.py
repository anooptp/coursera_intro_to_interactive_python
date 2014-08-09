# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
secret_num=0
low_num = 0
high_num = 100
guess_num = 0
max_guesses = 0


# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    global secret_num, max_guesses
    secret_num = random.randrange(low_num, high_num)
    max_guesses = int(math.ceil(math.log(high_num - low_num + 1, 2)))
    print 
    print "**** New Game ****"
    print "Range is from",low_num,"to",high_num
    print "Total guesses :",max_guesses
    print


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global low_num, high_num
    low_num = 0
    high_num = 100
    
    new_game()
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global low_num, high_num
    low_num = 0
    high_num = 1000
    
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    global guess_num, max_guesses
    try:
        max_guesses -= 1
        print "Number of guesses remaining :",max_guesses
        guess_num = int(guess)
    except ValueError:
        print "invalid num"
    if guess_num == secret_num:
        print "Correct"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "~~~ You Won ~~~ Congratulations ~~~"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print
        new_game()
    elif secret_num > guess_num:
        print "Higher"
    else:
        print "Lower"
        
    if max_guesses == 0:
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "~~~ You Lose ~~~ Try Again ~~~"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print
        new_game()



# create frame
frame=simplegui.create_frame("Guess the number", 200,200)

# register event handlers for control elements
inp = frame.add_input('Guess Number', input_guess, 100)
butRestart100 = frame.add_button('Range: 0 - 100', range100)
butRestart1000 = frame.add_button('Range: 0 - 1000', range1000)


# call new_game and start frame

new_game()

frame.start()


# always remember to check your completed program against the grading rubric
