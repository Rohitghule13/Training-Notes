# remove element function
def remove_elem(lis,string):
    for i in string:
        if i in lis:
            lis.remove(i)
    return lis 


lis = ['a','b','c','d','e','f'] # list 
string = "abklsa"             # string char is used to remove element available in list

print("Before Removing element in list : ",lis) #Print list Before element removing

lis = remove_elem(lis,string)

print("After Removing element in list : ",lis)  #Print list Before element removing