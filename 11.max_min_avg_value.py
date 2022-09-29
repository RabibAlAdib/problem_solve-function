# 11 maximum and minimum finder:

def finding_max_min(arry):
    size = len(arry)
    sum = 0
    min = arry[0]
    max = arry[0]
    for i in range(0, size):
        sum += arry[i]
        if arry[i] < min:
            min = arry[i]
        elif arry[i] > max:
            max = arry[i]
        else:
            pass
    print(f'max: {max} \nmin: {min} \nAvg: {round(float(sum/size),2)}')
    return max, min


# arry = [3, 5, 5]
arry = input("Enter the list: 0 0 0 0 0.. \n").split()
arry = [int(x) for x in arry]
finding_max_min(arry)
