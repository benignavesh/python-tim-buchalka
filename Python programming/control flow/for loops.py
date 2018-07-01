# # for i in range(1,20):
# #     print("i is now {}".format(i))
# # This is the common method to print the values in the for loop.
# # if we wish to find the length of a string we use "len(variable)".
# # For Eg:
# number = "98465986453865"
# print("{}".format(len(number)))
# # In python , the end character is automatically assigned to the \n so everytime we get the output in the next line. We can overwrite this thing by specifically mentioning the value.
number ="5,654,168,135,348,651"
cleanedNumber=''
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
# newNumber= int(cleanedNumber)
# print("The number is {} ".format(newNumber))
for char in number:
    if char in '0123456789':
        cleanedNumber= cleanedNumber + char
newNumber =int(cleanedNumber)
print("Te number is {}".format(newNumber))
# If we wish to write successive concatenations using for loop,
for game in ("football","basketball","cricket"):
    print("I like to play " + game)
# the correct format to use for loop is
# for i in range(initial value, final value, increment)
for i in range(0,101,5):
    print("Multiples of 5 :{} ".format(i))
    # TO CREATE nested for loop
for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i,j,i*j))
    print("=================================")