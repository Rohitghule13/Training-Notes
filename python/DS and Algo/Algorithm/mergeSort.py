def mergeSort(arr):
    if len(arr)>1:
        m = len(arr)//2

        l = arr[:m]

        r = arr[m:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0 

        while(len(l)>i)and(len(r)>j):
            if l[i]>r[j]:
                arr[k] = r[j]
                j += 1 
            else:
                arr[k] = l[i]
                i += 1 
            k += 1
        
        while(len(l)>i):
            arr[k] = l[i]
            i += 1 
            k += 1 
        
        while(len(r)>j):
            arr[k] = r[j] 
            j += 1
            k += 1 
        

arr = [4,3,1,2]
print("Before Sorting Array :- ",arr)
mergeSort(arr)
print("After Sorting Array :- ",arr)
