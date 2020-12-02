import sys
import math

def input() :
    filename = "input.data"
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def recurse(content, terms, summ, count, total):
    print(terms)
    for i in range(len(content)):
        term = int(content[i])
        new_summ = summ + term
        terms.append(term)
        if count < total:             
            recurse(content, terms, new_summ, count+1, total)
        if count == total and new_summ == 2020:
            print(terms, math.prod(terms))
            sys.exit()
        else:
            terms.remove(term) 

content = input()
recurse(content, [], 0, 0, 2)