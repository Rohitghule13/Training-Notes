 
# Merge Sort, in ascending order

def sort_here(array,left,right):
    i = j = k = 0  # set pointer for left array, right array and main array

    while(len(left)>i and len(right)>j): # comapring ledt and right half of array and merging in main array

        if left[i]>right[j]:    # left element is greater than right
            array[k] = right[j]  # condition is true merge right array in main array
            k += 1             # move pointer to ahead in main array 
            j += 1           # move pointer to ahead in right array 
            continue        # jump to the next ieration 

        array[k] = left[i] # when if codition gets fail swap left array element with main array 
        i += 1           
        k += 1   

    while(len(left)>i):   # if lef side of array element gets remain to merge in main array
        array[k] = left[i] # swap left array element in main array
        k += 1 
        i += 1 

    while(len(right)>j):   # if right side of array element gets remain to merge in main array
        array[k] = right[j] # swap right array element in main array
        j += 1 
        k += 1 
    return
def merge_sort(array):
   if len(array)>1:  # if array length is greater than 1 its true
 
       mid = len(array)//2  # get the middle point of array
 
       l = array[:mid]     # create left array
 
       r = array[mid:]     # create right array
 
       merge_sort(l)     # call left side of array
       merge_sort(r)

       sort_here(array,l,r)
    # return 0 # if gets false return 0
 
array = [4,3,2,1,5,6]
 
print("Before Sorting Array : ",array)
 
merge_sort(array)  # calling  function for sort array
 
print("After Sorting Array : ",array)
 
 
