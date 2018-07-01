# Write a program to append the time table to a new sample.txt
# In sample.txt, we want the tables from 2 to 12(similar to the output from the for loops part 2 in section 6)
# THe first column of numbers should right justified. As an example, the 2 times table should look like this :
# 1 times 2 is 2
# 2 times 2 is 4
# 3 times 2 is 6
# 4 times 2 is 8
# 5 times 2 is 10
# 6 times 2 is 12
# 7 times 2 is 14
# 8 times 2 is 16
# 9 times 2 is 18
# 10 times 2 is 20
# 11 times 2 is 22
# 12 times 2 is 24
#=-----------------------------

with open("C:/Users/PC/Desktop/Python Programming/ sample.txt", 'w') as table:
    for count in table:
        print(count+ "times 2 is " + {}.format(count) )







