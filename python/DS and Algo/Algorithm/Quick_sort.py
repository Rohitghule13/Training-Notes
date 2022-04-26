from platform import architecture
from re import A


def partition(array,low,high):
    pivot = array[high]
    i = low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1
def Quick_sort(array,low,high):
    if high>low:
        pi = partition(array,low,high)

        Quick_sort(array,low,pi-1)
        Quick_sort(array,pi+1,high)

array = [4,2,3,1]
print("Before array sorting :- ",array)
Quick_sort(array,0,len(array)-1)
print("After array Sorting :- ",array)