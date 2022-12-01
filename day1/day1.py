with open("input_day1.txt", "r") as f:
    list_input = f.read().split("\n")
    max = 0
    act = 0
    for x in list_input:
        if x != "":
            act += int(x)
        else:
            max = act if act > max else max
            act = 0
    print(max)