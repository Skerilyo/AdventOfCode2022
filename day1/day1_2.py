with open("input_day1.txt", "r") as f:
    list_input = f.read().split("\n")

    max = [0,0,0]
    act = 0
    for x in list_input:
        if x != "":
            act += int(x)
        else:
            max[0] = act if act > max[0] else max[0]
            max.sort()
            act = 0
    print(max)
    print(sum(max))