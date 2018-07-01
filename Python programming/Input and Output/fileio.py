# # we can open a file using the built in function in python called open(directory),<'file permissions'>
# jabber = open("C:/Users/PC/Desktop/sample.txt")
# for line in jabber:
#     if "jabberwork" in line.lower(): #.lower defines that we can use both the upper and lower case.
#         print(line, end='') #returns those lines having jabberwork in the file.
# jabber.close() # After we use the file, we close it using close() function.
# # If we put the file in the folder of the python file, then it can be directly accessed.
# with open("C:/Users/PC/Desktop/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='') # with () as variable is used to open certain file as the variable declared.
with open("C:/Users/PC/Desktop/sample.txt", 'r') as jabber:
    line = jabber.readline() # method to read SINGLE line
    while line:
        print(line, end='')
        line = jabber.readline()
with open("C:/Users/PC/Desktop/sample.txt", 'r') as jabber:
    lines = jabber.readlines() # method to read MULTIPLE line
print(lines)
# readlines created a list of all the lines.
