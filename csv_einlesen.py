with open("data.csv", "r") as csv_read:
    lines = csv_read.read().splitlines()
    print(lines)
    for i in lines:
        a = str(i.split(","))
        name = a[0]
        age = a[1]
        gender = a[2]
        print(a)
        #for element in a:
            #print(element)
            #print("{0} is {1} years old and {2}".format(element, element, element))
        #for e in i:
        #    print(e)
        #print("{0} is {1} years old and {2}".format(i, i, i))
