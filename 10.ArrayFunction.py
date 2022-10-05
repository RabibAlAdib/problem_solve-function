""" 10 """
"""
Qstn: Write a function that sorts an array of numbers.
In the main function, first create and print the unsorted array,
then use the function to sort the array, then print the sorted array.
Solution:
"""
import array


def sort_f(arry):
    x = sorted(arry)
    return x


inp = input("Enter the array list, by seperating with space: ").split()
lst= [int(x) for x in inp]
arry = array.array('i', lst)
sorted = array. array('i', sort_f(arry))
print("Unsorted Array: ", arry)
print("Sorted Array: ", sorted)
