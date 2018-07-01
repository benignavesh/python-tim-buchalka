# age=int(input("How old are you?"))
# # if(age>=16) and (age<=65):
# # This can also be written as
# # if 15< age <65:
# #     print("Hello!")
# # if you want to compare with either of the condition to be true, we can use or keyword.
# if (age>=18) or (age<=60):
#     print("Hello, adult!")
# else:
#     print("you're old/young.")
#
# # Any variable if assigned a number
#
# #if we do not write any condition to the if statement, then it automatically assumes to be true.
#
# x=int(input("How old are you?"))
# if x:
#     print("You are {} years old.".format(x))
#
# #not is used to negate any value
#
# age=int(input("How old are you?"))
# if not (age<18):
#     print("Hello adult")
# else:
#     print("Please come back after {} years".format(18-age))

# IF we want to use any character or a string to compare.

parrot="Norway"
letter=input("Enter a character")
if letter in parrot:
    print("The character is present in the string")
else:
    print("Oops, try again.")