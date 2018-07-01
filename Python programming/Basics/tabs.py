# name=input("Please enter your name:")
# age=int(input("How old are you, {}?".format(name)))
# print(age)
#
# if age >=18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {} years".format(18-age))
print("Please guess a number between 1 and 10")
guess=int(input())
if guess<5:
    print("Please guess higher")
    guess=int(input())
    if guess==5:
        print("Well done!!")
    else:
        print("Sorry, you haven't guessed correctly")
elif guess > 5:
    print("Please guess lower")
    guess=int(input())
    if guess==5:
        print("Well done!!")
    else:
        print("Sorry, you haven't guessed correctly")
else:
    print("You've got it the first time")