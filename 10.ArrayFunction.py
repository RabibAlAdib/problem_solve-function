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


arry = array.array('i', [5, 17, 8, 12, 7])
print("Unsorted Array: ", arry)
print("Sorted Array: ", sort_f(arry))
