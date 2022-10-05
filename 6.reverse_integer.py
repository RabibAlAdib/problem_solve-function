# 6  reverse number

def reverse_num(num):
    a = str(num)
    lst = []
    for x in a: 
        lst.append(x)
    reversed_lst = reversed(lst)
    for x in reversed_lst:
        print(int(x),end="")
    return
num = int(input("number: "))
reverse_num(num)



