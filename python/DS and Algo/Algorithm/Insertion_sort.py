'''This is inseration sort for ascending order '''
# define array 
array = [4,3,1,2]

print("Array Before Sorting :- ",array)
# set the loop for iteration
for i in range(1,len(array)):
    initial_val = array[i] # store the initial value for comparing

    j = i-1 # set the array index previous of the initial_val index
    
    while j>=0 and initial_val<array[j]: #comapre the follows the loop
        array[j+1] = array[j] # move ahead the element in array 
        j -= 1 

    array[j+1] = initial_val # store the element in initial_val to the value in j+1 

print("After Sorting Array (In Ascending Order) :- ",array)

'''This is inseration sort for Descending order '''
for i in range(1,len(array)):
    initial_val = array[i] # store the initial value for comparing

    j = i-1 # set the array index previous of the initial_val index
    
    while j>=0 and initial_val>array[j]: #compare and follow the loop when it is true
        array[j+1] = array[j] # move ahead the element in array 
        j -= 1 

    array[j+1] = initial_val # store the element in initial_val to the value in j+1 

print("After Sorting Array (In Descending Order) :- ",array)