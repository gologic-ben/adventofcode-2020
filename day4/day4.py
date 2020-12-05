import math, re

def input(filename) :
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

rows = input("input1.data")
valids = 0
mandatory_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]    # ,"cid"

# for chaque ligne
def scan(rows, start, end):
    #print("\r\nScanning from ", start, end)
    passkeys = []
    passvalues = {}
    passport = ""
    line = start
    while line <= end:
        passport += " " + rows[line] 
        for fields in rows[line].split(" "):
            fieldkey = fields.split(":")[0]
            passkeys.append(fieldkey)
            passvalues[fieldkey] = fields.split(":")[1]
        line += 1
    for k in mandatory_keys:
        if k not in passkeys:
            return False
        else:
            # PART TWO
            #    byr (Birth Year) - four digits; at least 1920 and at most 2002.
            #    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            #    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            #    hgt (Height) - a number followed by either cm or in:
            #        If cm, the number must be at least 150 and at most 193.
            #        If in, the number must be at least 59 and at most 76.
            #    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            #    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            #    pid (Passport ID) - a nine-digit number, including leading zeroes.
            if k == "byr":
                if not (len(passvalues[k]) == 4 and int(passvalues[k]) >= 1920 and int(passvalues[k]) <= 2002): return False
            if k == "iyr":
                if not (len(passvalues[k]) == 4 and int(passvalues[k]) >= 2010 and int(passvalues[k]) <= 2020): return False
            if k == "eyr":
                if not (len(passvalues[k]) == 4 and int(passvalues[k]) >= 2020 and int(passvalues[k]) <= 2030): return False
            if k == "hgt":
                if passvalues[k][-2:] == "cm" and not (int(passvalues[k][:-2]) >= 150 and int(passvalues[k][:-2]) <= 193): return False
                if passvalues[k][-2:] == "in" and not (int(passvalues[k][:-2]) >= 59 and int(passvalues[k][:-2]) <= 76): return False
                if passvalues[k][-2:] not in ["cm","in"]: return False
            if k == "hcl":
                if re.match(r'^\#[0-9a-f]{6}$', passvalues[k]) is None: return False
            if k == "ecl":
                if passvalues[k] not in ["amb","blu","brn","gry","grn","hzl","oth"]: return False
            if k == "pid":
                if re.match(r'^\d{9}$', passvalues[k]) is None: return False
    print(passvalues)
    return True

# search for each passports
start = 0
p = 0
for i in range(len(rows)):
    if rows[i] == "":
        p+=1
        end = i-1
        if scan(rows, start, end):
            valids +=1
        start = i+1
    if i == len(rows) - 1 and scan(rows, start, i):
        valids +=1

print("\r\nvalids", valids, "on", p)