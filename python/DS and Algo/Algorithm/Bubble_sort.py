'''Bubble sort algorithm to '''
array = [9,2,8,6,7,1,4,3,5] # defining array 
# we are used two loop for sorting arrayy

print("Before Sorting :- ",array) 

for i in range(len(array)-1): # this is outer loop for iterate inner loop

    for j in range(len(array)-i-1): # this is inner loop for sort array in ascending order 

        if array[j]>array[j+1]: # condition which is greater index element is less than smaller index element so exchange the element 

            array[j],array[j+1] = array[j+1],array[j] # exchange elemet to specific index 

print("After Sorting (in ascending order):- ",array)

for i in range(len(array)-1): # this is outer loop for iterate inner loop

    for j in range(len(array)-i-1): # this is inner loop for sort array in ascending order 

        if array[j]<array[j+1]: # condition which is greater index element is gereter than smaller index element so exchange the element 

            array[j],array[j+1] = array[j+1],array[j] # exchange elemet to specific index 

print("After Sorting (in descending order):- ",array)
