# ***** 4 *****
def c_digits(number):
    length = 0
    for i in str(number):

        # print(i, end=' ')
        length += 1
    return length


number = int(input("Enter the number: "))
print("The length of given number: ", c_digits(number))


# other way
# def digits(number):
#     return len(number)

# number = input("Enter the number: ")
# print("The length of given number: ", digits(number))








