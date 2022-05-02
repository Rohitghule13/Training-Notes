''' this is the selection sorting algorithm to make an array element in 
ascending order 
'''
# define the array 
array = [22,11,44,55,33]

print("before sorting array :- ",array) # display array before sorting
# iterate loop for checking 
for i in range(len(array)-1):
    min_index = i # select the element index to compare with others

    for j in range(i+1,len(array)): # this is loop used for compare the selected element with others through iteration rest of array

        if(array[i]>array[j]): # compare if it is less by selected element this condition gets true
            min_index = j # add less element index here 

    array[i],array[min_index] = array[min_index],array[i] # exchange element here 

print("After sorting array (In ascending Order) :- ",array) # Display array in ascending order 

''' now we want array in desending order so we just change the condition according '''
for i in range(len(array)-1):
    min_index = i # select the element index to compare with others

    for j in range(i+1,len(array)): # thiss is loop used for compare the selected element with others through iteration rest of array

        if(array[i]<array[j]): # compare if it is more than selected element this condition gets true
            min_index = j # add less element index here 

    array[i],array[min_index] = array[min_index],array[i] # exchange element here 

print("After sorting array (In Descending Order):- ",array)