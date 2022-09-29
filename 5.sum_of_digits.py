# ******* 4 ********

def sum_digit(number):
    s = 0
    for i in str(number):
        s = s + int(i)
    return s


number = int(input("Enter any number: "))

digit = sum_digit(number)
print("Sum: ",digit)


