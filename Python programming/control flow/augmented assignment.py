number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123465789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is : {}".format(newNumber))
# Augmented assignment is like the shorthand notation used in other languages, $ # except in python it is a lot more efficient way to handle augmented assignments.
# cleanedNumber += number[i]

x = 23
x += 24
print(x)
# In python, ** represents to the power of.
# For eg.
x **= 2 # Here 47 raised to the power 2 is executed.
print(x)
# Also used for concatenation purposes.
greeting = "Hello"
greeting += " Sir"
print(greeting)