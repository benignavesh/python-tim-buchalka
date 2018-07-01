ip=input("Enter your IP Address")
ip += '.'
segment = 1
segment_length=0
for character in ip:
    if character == '.':
        print("Segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1


