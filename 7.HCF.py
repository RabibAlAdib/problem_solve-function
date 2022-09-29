# 7 HCF

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


x,y = input("Enter the number: ").split()
x,y = int(x), int(y)
print("HCF of", x, "and", y, "is:", hcf(x,y))