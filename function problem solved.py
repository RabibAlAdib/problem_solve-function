""" """


# ******1******
#
# def triangle(number, symbol):
#     n = 10
#     for i in range(number):
#         print(' '*n , end="")
#         print(f'{symbol} '*i )
#         n-=1
# number = int(input("Number: "))
# symbol = input("Symbol: ")
# triangle(number,symbol)
#
# ********same*************

# def triangle(num , sym):
#     for i in range(num):
#         for j in range(i+1):
#             print(f' {sym} ', end='')
#         print()
#
#
# num=int(input())
# sym=input()
# triangle(num , sym)


# *******2********
#
# def sphere(radius):
#     v=(4/3)*(3.1416)*(radius*radius*radius)
#     print(v)
#     return v
#
# radius=int(input())
# sphere(radius)


# *******3*******
#
# def perameter(num):
#     a=1
#     for i in range(num):
#         a= a*(i+1)
#         print( i,a)
#     return a
#
# num=int(input("Enter the number : "))
# print(f"Factorial of {num} is ", perameter(num))


# *****4*****

def digits(number):
    print(len(number))


number = input("Enter the number: ")
digits(number)


# ******3******
# def factorial(num):
#     a=1
#     for i in range(num):
#         a = a*(i+1)
#         print(a)
#     return a
#
# num=int(input())
# print("enter the number : ",factorial(num))


# ********* 4 ********
def sum_digit(number):
    s = 0
    for i in str(number):
        s = s + int(i)
    return s


number = int(input("Enter any number: "))

digit = sum_digit(number)
print("Sum: ", digit)



# 5
# def integer(num):
#     sum=0
#     while num>0:
#         x=num%10
#         a=num//10
#         sum=sum+x
#         print(sum)
#         break
#     return sum
# num=int(input("enter the number : "))
# integer(num)


# n=0
# while n<10:
#     print(n)
#     n=n+1


# 6  reverse number
# def rvrc(num):
#     rvrc_done = reversed(num)
#     for x in rvrc_done:
#         print(x, end=' ')
#     return rvrc_done
#
#
# num = list(map(int, input("NUmber: ").split()))
# rvrc(num)

# try
# def reverse_num2(num):
#     number_split = []
#     reverse_done = []
#     for i in str(num):
#         number_split.append(i)
#     for i in number_split:
#         reverse_done.append(number_split[-i])
#     print(reverse_done)
#     return reverse_done
#
#
# num = int(input("Enter number without space: "))
# print(reverse_num2(num))


# 7 HCF
# def hcf(x,y):
#     if x>y:
#         smaller = y
#     else:
#         smaller = x
#
#     for i in range(1,smaller+1):
#         if (x%i== 0) and (y%i == 0):
#             hcf = i
#
#     return hcf

# 8 LCM
# def lcm(x,y):
#     if x>y:
#         greater = y
#     else:
#         greater = x
#
#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#
#     return lcm
#
# x,y = input("Enter the number: ").split()
# x,y = int(x), int(y)
# print("HCF of", x, "and", y, "is:", hcf(x,y))
# print("LCM of", x, "and", y, "is:", lcm(x,y))


# import math as ma

# print("HCF of", x, "and", y, "is:", ma.gcd(x,y))
# print("lCM of", x, "and", y, "is:", ma.lcm(x,y))


# 9
"""
Palindromic Number:
Palindrome: Remains the same when its digits are reversed.

Example:    dad civic malayalam  101  7667 5 
            42 + 24 = 66                     66 palindrome number
            35 + 53 = 88                     88    "
            67 + 76 = 143 + 341 = 484  
"""

'''
Perfect Number:
    A positive integer that is equal to the sum of its proper divisors. 
    The smallest perfect number is 6, which is the sum of 1, 2, and 3.
    Other perfect numbers are 28, 496, and 8,128
6, 28, 496, 8128
'''

# def prime(num):
#     prime = True
#     for i in range(2, num):
#         if(num%i == 0):
#             prime = False
#             return False
#     if prime:
#         return f"{num} number is Prime" , True
#     else:
#         return f"{num} number is not Prime", False
#
# def palindrome(num):
#     num = int(input("Number: "))
#     revese = int(str(num)[::-1])
#     if num == revese:
#         return f"{num}, is a Palindrome Number."
#     else:
#         return f"{num}, is not a Palindrome Number."
#
#
# def perfect(num):
#     count = 0
#     for i in range(1, num):
#         if num % i == 0:
#             count = count + i
#     if count == num:
#         return f'The number {num} is a Perfect number! \n'
#     else:
#         return f'The number {num} is not a Perfect number! \n'


# nums = int(input("Please enter the number: "))
# num = nums
# print('checking Prime or Not..')
# print(prime(num))
#
# print("\n checking Perfect Number or Not...")
# print(perfect(num))
#
# print("\n checking palindromes Number or Not...")
# print(palindrome(num))

# 10. Write a function that sorts an array of numbers.
# In the main function, first create and print the unsorted array,
# then use the function to sort the array, then print the sorted array.
# Solution:
#
# import array
#
#
# def sort_f(arry):
#     x = sorted(arry)
#     return x
#
#
# arry = array.array('i', [5, 17, 8, 12, 7])
# print("Unsorted Array: ", arry)
# print("Sorted Array: ",sort_f(arry))


# 11 maximum and minimum finder:

# def finding_max_min(arry):
#     size = len(arry)
#     sum = 0
#     min = arry[0]
#     max = arry[0]
#     for i in range(0, size):
#         # sum += arry[i]
#         if arry[i] < min:
#             min = arry[i]
#         elif arry[i] > max:
#             max = arry[i]
#         else:
#             pass
#     print(f'max: {max} \n min: {min}')
#     return max, min
#
#
# arry = [50, 40, 30, 40, 5]
# finding_max_min(arry)


# 12 Total Word Checker
# def word_finder(str):
#     string = str.split()
#     return len(string)
#
#
# str = input("Enter your text: ")
# print(word_finder(str))

# 13 Convert string to Upper case
# def upper(str):
#     return str.upper()
#
#
# str = input("Enter your text: ")
# print("Updated string: ", upper(str))


# 14 check student varify
# def valid(id):
#     if id in student_list:
#         return True
#     else:
#         return False
#
#
# student_list = [2221001, 2221002, 2221003,222104]
# id = int(input("Enter your Student Id: "))
# print(valid(id))

# 15
# def doc():
#     return 'The answer to life the universe and everything'
#
#
# print(doc())
