import sys
import math

def input(filename) :
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

passwords = []
content = input("input2.data")
for i in range(len(content)):
    c = content[i]
    split1 = c.split(' ')
    split_range = split1[0].split('-')
    occ = 0
    m = int(split_range[0])  # min
    M = int(split_range[1])  # max
    search = split1[1][0]   # a
    passwd = split1[2]
    print("checking input:", m, M, search, passwd)
    # star 1
    '''
    for l in passwd:
        if l == search: occ += 1
    if occ >= m and occ <= M:
        passwords.append(passwd)
    '''
    # star 2
    for l in range(0, len(passwd)): 
        if m == l+1 and passwd[l] == search: occ +=1
        if M == l+1 and passwd[l] == search: occ +=1
    if occ == 1: passwords.append(passwd)
    
print(passwords)
print(len(passwords))
