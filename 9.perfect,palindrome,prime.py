""" 9 """
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
    perfect numbers form range(1,10000) are: 6, 28, 496, 8128

'''

def prime(num):
    prime = True
    for i in range(2, num):
        if(num%i == 0):
            prime = False
            return False
    if prime:
        return True
    else:
        return False

def palindrome(num):

    revese = int(str(num)[::-1])
    if num == revese:
        return f"{num}, is a Palindrome Number."
    else:
        return f"{num}, is not a Palindrome Number."


def perfect(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count = count + i
    if count == num:
        return f'The number {num} is a Perfect number! \n'
    else:
        return f'The number {num} is not a Perfect number! \n'


nums = int(input("Please enter the number: "))
num = nums
print('checking Prime or Not..')
print(prime(num))

print("\n checking Perfect Number or Not...")
print(perfect(num))

print("\n checking palindromes Number or Not...")
print(palindrome(num))