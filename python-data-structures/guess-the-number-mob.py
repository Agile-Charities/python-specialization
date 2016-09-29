"""
Mob programming exercise

Single player guess-the-number that tracks, per person (give a name), how many
guesses it takes to guess the number. This information is stored in a local
text file, and stores data in the form
    Tyler: [5,3,7,9,2,6,3]
    Dennis: [6,3,4,7,5,3,6]

The program will do the following (order may change):

- NOT DONE - prompt for a username
- NOT DONE - read in the data (store in dict { "username": [# of guesses] }
    - NOT DONE - need a dictionary
    - NOT DONE - need a file
    - NOT DONE - need to know how data is stored (above)
- NOT DONE  - display username's average so far
- DONE     - get a random number
- DONE     - do the guessing game
- NOT DONE - Too high? Too low?
- NOT DONE - display change in average

Optional features:
- NOT DONE - write the updated data to the file, overwriting the old data
-            handler.write("text\n")
- NOT DONE - prompt for another game, or quit

"""

# randint(1,10) produces a number between 1 and 10, inclusive
from random import randint

# Make sure the input is a number between 1 and 10 (inclusive)
def check_input(inp, player_name):
    # make sure the input is a number
    try:
        n = int(inp)
    except:
        print "ERROR: Player " + player_name + " did not enter an integer."
        quit()

    # make sure the number is between 1 and 10
    if n < 1 or n > 10:
        print "ERROR: Player " + player_name + " did not enter a number between 1 and 10"
        quit()

    return n


# place to store the data
player_data = dict()

# read the data from player_data.txt
data_store = open("player_data.txt")

# put the info from the file into the dictionary
# this requires parsing each line of the file


# Get this game's random number
num = randint(1,10)

# We can keep track of how many guesses were needed
counter = 0

# Get the player's name


# display the player's average, if it exists


# the game
while True:
    guess_txt = raw_input(player_name + ", guess a number between 1 and 10: ")
    guess = check_input(guess_txt, player_name)

    # increment this with every new guess
    counter += 1

    if guess == num:
        print "Correct! " + player_name + " wins after " + str(counter) + " guesses!"
        break
    else:
        print "Incorrect, try again!"
        # tell the player if their guess was too high or too low


# display the new average


# thank the player for playing
print "Thanks for playing, " + player_name + "!"











