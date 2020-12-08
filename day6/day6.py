import math, re

def input(filename) :
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

'''
This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
'''

'''
This list represents answers from five groups:

    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
'''

def findAnswersByGroup(answers, row):
    for i in row:
        if i in answers:
            answers[i] += 1
        else:
            answers[i] = 1
    return answers

rows = input("input2.data")
groups = []
answers = {}
peoples = []
people = 0
for i in rows:
    if i != "":
        people += 1
        answers = findAnswersByGroup(answers, i)
    if i == "":
        #print("group answers", people, answers)
        groups.append(answers)
        peoples.append(people)
        answers = {}
        people = 0

# last one
groups.append(answers)
peoples.append(people)

print("groups", groups)
print("peoples", peoples)

Sum = 0
for i in range(len(groups)):
    group = groups[i]
    for key in group.keys():
        count = group[key]
        if peoples[i] == count:
            Sum += 1

print("\r\nanswer", Sum)