# Iterators are used to return one element in a list each time.
# string = "123465879"
# for char in string:
#     print(char)
# Here the characters of the string are stored in an array in the computer memory,
# so the iterator char is traversing the array and printing each element from the array of string.
# To see what's going in the memory part of the iteration,

# my_iterator = iter(string)
# print(my_iterator)
# #prints the address of the iterator of string
# print(next(my_iterator))
# #increases the address of iterator with one size
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# # Here the error pops out for stopping the iteration, since we have encountered all the elements.'
# the for loop overcomes this problem, by that as soon as it encounters the StopIteration it stops the next() function.

string1="qwertyuiop"
my_iter=iter(string1)

for count in string1:
    print(next(my_iter))
print(len(string1))