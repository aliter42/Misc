# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random


# initialize global variables used in your code
secret_num = 0
rem_guess = 0


# helper function to start and restart the game
def new_game(rand_play):
    
    print "New Game! Get Set Go!"
    
    if (rand_play == 0):
        range100()
    else:
        range1000()
    
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_num, rem_guess
    secret_num = random.randrange(0,100)
    rem_guess = 7
    print "Range is 0 - 100"
    print "Guesses remaining: ", rem_guess
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_num, rem_guess
    secret_num = random.randrange(0,1000)
    rem_guess = 10
    print "Range is 0 - 1000"
    print "Guesses remaining: ", rem_guess

    
def input_guess(guess):
    # main game logic goes here	
    global player_guess, rem_guess
    player_guess = int(guess)
    rem_guess -= 1
    
    if rem_guess <= 0:
        print "Bad luck! The secret number is", secret_num
        new_game(0)
        
    
    print "Your guess:", player_guess
    print rem_guess, "guesses remaining"
    
    if player_guess > secret_num:
        print "Guess lower!"
    elif secret_num > player_guess:
        print "Guess higher!"
    else: 
        #number == my_guess:
        print "Bazinga! The number is ", sec_number
        new_game(1)
      
    
    
    
# create frame

f = simplegui.create_frame("Guess the Number!", 300, 300)




# register event handlers for control elements

f.add_button("Let Range be [0-100]", range100, 150)
f.add_button("Let Range be [0-1000]", range1000, 150)
f.add_input("Guess the number", input_guess, 100)


# call new_game and start frame

f.start()
new_game(0)