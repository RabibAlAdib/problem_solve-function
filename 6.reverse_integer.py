# 6  reverse number

def reverse_num(num):
    reverse_done = reversed(num)
    for x in reverse_done:
        print(x, end=' ')
    return reverse_done


num = list(map(int, input("NUmber: ").split()))
reverse_num(num)



