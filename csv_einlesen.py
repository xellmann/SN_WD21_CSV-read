with open("data.csv", "r") as csv_read:
    lines = csv_read.read().splitlines()
    print(lines)
    for i in lines:
        a = i.split(",")
        name = a[0]
        age = a[1]
        gender = a[2]
        print(name + " is " + age + " years old and " + gender)
