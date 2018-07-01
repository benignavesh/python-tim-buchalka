#Ranges are used in for loops
# In python 3, it is built-in type, but in python 2 it was a function


print(range(100)) # Displays the range object till 100.

mylist = list(range(10))
print( mylist) #Here the range object passes the elements into a list stored in variable mylist.

even=list(range(0,10,2)) # range(initiation, end, step)
odd=list(range(1,10,2))

print(even)
print(odd)
# xRange in python 2 ~ range in python 3


# .index returns the character's position in a list
mystr ="qwertyuiop"
print(mystr.index("e"))
odd=range(1,10000,2)
print(odd[960]) #displays the 960th index element in the odd list

#Divisibility test

sevens=range(7,1000,7)
x=int(input("Enter a number less than 1000 : "))
if x in sevens:
    print(" {} is divisible by 7".format(x))
# We can slice a range to get a specific number of elements.
decimals=range(0,100)
three=decimals[3:40:3]
for i in three:
    print(i)
print('=' * 40)
for i in range(3,40,3):
    print(i)

print(three == range(3,40,3))
# Since the list contains same elements.

r=range(0,100)
for i in r[::-2]:
#This command starts from the last and counts -2
    print(i)
for i in range(99,0,-2):
    print(i)

# Back slicing a list or range is very powerful tool

backString= "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])
# prints the elements of the string in reverse order

