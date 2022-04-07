def check__string(st):
    speacial = "!@#$%^&*"
    if any(a for a in st if a.islower()):
        if any(a for a in st if a.isupper()):
            if any(a for a in st if a.isdigit()):
                if any(a for a in st if a in speacial):
                    return True 
                    ''' return true if string contain speacial char, digit
                    lower and upper case'''
    return False # or return false

dictionary = {"elem1": "ROhit!21","elem2": "slkdw12","elem3": "akjsa","elem4": "fros"}
# created Dictionary with key and random values

unique = [] # List is for to store Unique item 

#for loop for get values from dictinary
for i in dictionary.values():
    if check__string(i):
        unique.append(i)

print("Unique Item : ", unique) #Display unique item
