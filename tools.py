def load(filename) :
    print("importing data from " + filename)
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content