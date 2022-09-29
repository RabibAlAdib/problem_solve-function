# ******1******

def triangle(num, sym):
    for i in range(num):
        for j in range(i + 1):
            print(f' {sym} ', end='')
        print()


num = int(input("Enter the number of line: "))
sym = input("Enter shape: ")

triangle(num, sym)

# ******** Equilibrium Triangle *************

# def triangle(number, symbol):
#     n = 10
#     for i in range(number):
#         print(' '*n , end="")
#         print(f'{symbol} '*i )
#         n-=1
#
#
# number = int(input("Number: "))
# symbol = input("Symbol: ")
# triangle(number,symbol)
