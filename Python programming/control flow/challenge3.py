# Modify the program below to use a while loop to allow as many guesses as necessary.
#
# The program should let the player know whether to guess higher or lower, and should print a message when the guess is correct. A correct guess will terminate the program.
#
# As an optional extra, allow the player to quit by entering 0 (zero)  for their guess.

number = 8
guess=int(input("Guess a number :"))
while( number != guess):
    if( guess< number):
        guess=int(input("Guess higher : "))
    elif( guess > number):
        guess=int(input("Guess lower :"))
    elif( guess == 0):
        break
print("Woah! You guessed right!")