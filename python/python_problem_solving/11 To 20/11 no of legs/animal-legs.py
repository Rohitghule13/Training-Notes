def counted(chicken,pigs,cows):
    totallegs= (chicken*2)+(pigs*4)+(cows*4)
    ''' logic is chicken have 2 legs so number of chicken multiply of having chicken legs
    and other animal apply same logic'''

    return totallegs # return total legs

chicken = 2 # chicken var contain number of chicken 
pigs = 4    # pigs var contain number of pigs 
cows = 4    # cows var contain number of cows 
print("legs are : ",counted(chicken,pigs,cows)) # calling function