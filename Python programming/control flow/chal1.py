# Write a small program to ask for a name and an age. When both the values have been entered, check if the person is right age to go on a 18-30 holiday(they must he over 18 and under 31).
#     If they are, welcome them to the holiday, otherwise print a polite message refusing them entry.
name=input("Hello, What's your good name, ?")
age=int(input("How old are you, {}?".format(name)))
if (age>18) and(age<31):
    print("Dear {}, You're welcome to the holiday, ENJOY! :)".format(name))
else:
    print("Sorry, this party isn't for you, better luck next year. :)")