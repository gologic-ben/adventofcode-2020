import math

def input(filename) :
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

rows = input("input2.data")

# for chaque ligne
def slopes(right, down):
    i = 0
    trees = 0
    line = 0
    currentColumn = 0
    # print("Sliding",len(rows)," rows")
    while line < len(rows):
        # On arrive au bout de la ligne, il faut repeter la ligne a la fin de chaque ligne
        if currentColumn+right >= len(rows[line]) :
            for i in range(len(rows)):
                rows[i]+=rows[i]
                # print("Extending", rows[i])

        # print("sliding to",line+down,currentColumn+right,rows[line+down],rows[line+down][currentColumn+right])
        if rows[line+down][currentColumn+right] == "#":
            trees += 1
        currentColumn += right
        line += down
        if line+down >= len(rows):
            print("Hit", trees)
            line += down
    return trees
'''
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2
'''
trees = []
trees.append(slopes(1,1))
trees.append(slopes(3,1))
trees.append(slopes(5,1))
trees.append(slopes(7,1))
trees.append(slopes(1,2))
print("Hit trees", trees, math.prod(trees))