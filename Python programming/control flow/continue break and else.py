shopping_list = ["milk","pasta","eggs","spam","bread","rice"]
for item in shopping_list:
    # print("Buy " + item)
    # continue keyword is used to check a condition if the condition is true, then bypass the line.

    # if item=='spam':
    #     continue
    #
    # print("Buy " + item)

 #Here,Buy Spam is not executed, since the if statement gets true #and continue is executed and the print statement is #bypassed/skipped.
 # moved back to line before and hence the for loop continues.

#Break on the other hand is used to break/terminate any loop or process.
    if item == 'spam':
        break
    print("Buy " + item)

# If we remove spam from the list, we get an error.
meal=["egg","bacon","tomato","sausages"]
# for item in meal:
#     if item=='spam':
#         nasty_food_item=item
#         break
# if nasty_food_item=='spam':
#     print("Can't have anything to eat?")
    #NameError: name 'nasty_food_item' is not defined
# We get this error because nasty_food_item is not defined here.
# What we do is initialize nasty_food_item before entering the for loop.
nasty_food_item=''
for item in meal:
    if item=='spam':
        nasty_food_item=item
        break
else:
        print("Oops!")
if nasty_food_item=='spam':
    print("Can't have anything to eat?")

# else is used specifically for the element with the if condition, after break is executed.
# VARIABLES ARE CASE SENSITIVE.