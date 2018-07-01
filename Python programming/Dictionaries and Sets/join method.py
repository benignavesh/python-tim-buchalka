myList = ("a", "b", "c", "d")
newString = ''
# for c in myList:
#     newString+= c + ","
# Instead of using the above code to join the elements of myString to
#  form a single string, we can directly use the following code :
newString = ",".join(myList)
# .join no longer requires a loop so we can omit the for line
print(newString)
letters = "qwertyuiop"
newString2 = ",".join(letters)
print(newString2)