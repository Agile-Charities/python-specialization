"""
Mob programming exercise

Single player guess-the-number that tracks, per person (give a name), how many
guesses it takes to guess the number. This information is stored in a local
text file, and stores data in the form
    Tyler: [5,3,7,9,2,6,3]
    Dennis: [6,3,4,7,5,3,6]

The program will do the following (order may change):

- DONE     - prompt for a username
- DONE     - read in the data (store in dict { username: [# of guesses] }
    - DONE     - need a dictionary
    - DONE     - need a file
    - DONE     - need to know how data is stored (above)
- DONE     - display username's average so far
- DONE     - get a random number
- DONE     - do the guessing game
- DONE     - Too high? Too low?
- DONE     - display change in average
- NOT DONE - write the updated data to the file, overwriting the old data
-            handler.write("text\n")

Optional features:

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


# store the data
player_data = dict()

# read the data from player_data.txt
data_store = open("player_data.txt")

# put the info from the file into the dictionary
for line in data_store:
    # clean the line of newlines and spaces
    line = line.strip()
    parts = line.split()
    
    # grab the key
    key = parts[0][0:len(parts[0]) - 1]
    
    # grab the list of nums
    no_brackets = parts[1][1:len(parts[1]) - 1]
    split_nums = no_brackets.split(",")
    list_of_nums = []
    for char in split_nums:
        num = int(char)
        list_of_nums.append(num)
        
    # add the data to our dictionary
    player_data[key] = list_of_nums

# Get this game's random number
num = randint(1,10)

# We can keep track of how many guesses were needed
counter = 0

# Get the player's name
player_name = raw_input("Player, please enter your name: ")

# display the player's average, if it exists
if (player_data.has_key(player_name)):
    print "Average equals: " + str(sum(player_data[player_name]) / float(len(player_data[player_name])))
else:
    print "Welcome to the game!"

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
        if guess > num:
            print "Your guess was too high."
        else:
            print "Your guess was too low."

# display the new average
player_data[player_name].append(counter)
print "New Average: " + str(sum(player_data[player_name]) / float(len(player_data[player_name])))

print "Thanks for playing, " + player_name + "!"











