def array_string(st):   # function for checking string of array containing digit
    arr = [] # create array for store string digit contain 

    num = "1234567890" # var is used for reference for checking digit 

    for i in st:
        if any(c for c in i if c in num):
            arr.append(i)

    return arr # return array string which is digit contain
    
# create string of array
st = ["Rohit","kajska","asjakw","ajwh12"]

# call function for check digit contain string in array
print(array_string(st))