# Quick SOrt algorithm. sorting array in ascending order
 
def partition(array,l,h): # partition function compare arrays element using pivot
 
   pi = array[h] # choose pivot as highest index order element in array
 
   print(pi)
 
   i = l - 1 # set array pointer here
 
   for j in range(l,h): # loop for checking element in array
 
       if array[j]<=pi: # condition set array in ascending order
 
           i += 1 # moving array poinnter ahead
 
           array[i],array[j] = array[j],array[i] # swap element
 
   print(f"unsorted in paratition low {l} high {h} : {array}")
 
   i += 1 # move array pointer ahead
 
   array[i],array[h] = pi,array[i] # swap array element with array pointer and pivot
 
   print(f"sorted in paratition low {l} high {h} : {array}")
   return i
 
def Quick_sort(array,l,h):
   if l<h: # check weather the array isnt empty
 
       pi = partition(array,l,h) # call partition with array and low and high value
 
       Quick_sort(array,pi+1,h) # call recursivelly with decrement high value
 
       Quick_sort(array,l,pi-1) # call recursivelly with increment low value
 
       # these recursive function call with specific high and low value decreement and increment order
       # which helps to sort,decide loop iteration and used to select pivot hence it also helps to breaking the
       # recursive loop
   pass
 
 
array = [4,2,3,5,1,6] # array element
 
print(array) # print orignal array
 
Quick_sort(array,0,len(array)-1) # call sorting function
 
print(array) # print ascending order sorted array
