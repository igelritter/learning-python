#This is basically a text style adventure. Each room is defined as a function
#as well as the starting and dying text.

#importing the exit function
from sys import exit

#gold room.
def gold_room():
    print "This room is full of gold. How much do you take?"
    next=(raw_input(">"))
#This 'if/else' statement is broken. It will only accept numbers with 1 or 0
#It does very little to figure out whether the user entered numbers or a string
    
##    if "0" in next or "1" in next:
##        how_much=int(next)
##    else:
##        dead("Man, learn to type a number.")
    
#what we need here is a try/except block. The try except attempts to convert the
#inputed string into an int. If it succeeds, then the int is evaluated for
#the next condition; if not, then the user gets a homemade error message--they die--
#and the program terminates.
    
    try: 
        how_much=int(next)
    except:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        EXIT (0)
    else:
        dead("You greedy bastard!")

#bear room
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    while True:
        next = raw_input(">")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

# cthulu room
def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He...it...whatever...stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    next = raw_input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        cthulu_room()

#dead() and start() functions
def dead(why):
    print why,"Good job!"
    exit (0)
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    next = raw_input(">")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("you stumble around the room until you starve.")
#after all the function definitions, we get to the function call that starts
#the program
start()

    
