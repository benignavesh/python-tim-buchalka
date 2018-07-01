import random
highest=10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    if guess<answer :
        print("Please guess higher")
    else: # guess must be lower
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Well done, you've guessed it right.")
    else:
        print("Sorry, Bad Day!")

else:
    print("You got it the first time!")