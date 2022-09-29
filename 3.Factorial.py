# ******* 3 *******

def perameter(num):
    a = 1
    for i in range(num):
        a = a * (i + 1)
        # print( i,a)   # for self understanding the process
    return a


num = int(input("Enter the number : "))
print(f"Factorial of {num} is ", perameter(num))
