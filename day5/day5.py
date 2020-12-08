import math, re

def input(filename) :
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

'''
For example, consider just the first seven characters of FBFBBFFRLR:
    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

For example, consider just the last 3 characters of FBFBBFFRLR:
    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.
'''

def findSeatID(seat):
    min = 0
    max = 127
    left = 0
    right = 7
    row = 0
    column = 0
    for x in range( len(seat) ):
        i = seat[x]        
        if i == "F":
            max = math.floor((max+min)/2)
        if i == "B":
            min = math.ceil((max+min)/2)
        if i == "L":
            right = math.floor((left+right)/2)
            #print("right", left, right)
        if i == "R":
            left = math.ceil((left+right)/2)
            #print("left", left, right)
        if x == len(seat) - 4:  # last row
            if i == "F": row = min
            if i == "B": row = max
            #print("last row", x, i, min, max, left, right, row, column)
        if x == len(seat) - 1:  # last column
            #print("last column", x, i, min, max, left, right, row, column)
            if i == "L": column = left
            if i == "R": column = right            

    #print(min, max, left, right, row, column)
    seatId = row * 8 + column
    return seatId

rows = input("input2.data")
seats = []
for i in rows:
    seats.append(findSeatID(i))

seats.sort()
for i in seats:
    if i-1 not in seats:
        print("i-1 not in seats:", i-1)
    if i+1 not in seats:
        print("i+1 not in seats:", i+1)
print("\r\nanswer", max(seats), seats)