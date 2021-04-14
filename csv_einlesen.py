with open("data.csv", "r") as csv_read:
    lines = csv_read.read().splitlines()
    for i in lines:
        a = i.split(",")
        print("{0} is {1} years old and {2}".format(a[0], a[1], a[2]))
