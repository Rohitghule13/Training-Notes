def return_length(num):
    num_st = str(num) #it convert integer into string 
    count = 0         #count variable for counting 
    for i in num_st:  #iterate string till last char
        count += 1    #count iterater loop
    return count      #return count

num = int(input("enter the number : "))
print(return_length(num))