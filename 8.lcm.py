# 8 LCM
def lcm(x, y):
    if x > y:
        greater = y
    else:
        greater = x

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


x, y = input("Enter the number: ").split()
x, y = int(x), int(y)

print("LCM of", x, "and", y, "is:", lcm(x, y))
