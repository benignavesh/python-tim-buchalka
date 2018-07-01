ip=input("Enter your IP Address")

segment=1 # Since there must be atleast one segment.
segment_length=0
character="" #initialized.
for character in ip:
    if character=='.':
        print("Segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in the string was a . , then we haven't printed the last segment
if character!='.':
    print("segment {} contains {} characters".format(segment, segment_length))
# THe following code executes correctly except if the input is left blank. This is because character is not initialized if the for loop is not executed even once. Thus, we need to initialize the character variable once to avoid this error.

