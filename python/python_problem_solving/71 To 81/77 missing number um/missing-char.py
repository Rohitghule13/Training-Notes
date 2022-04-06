# function to find out character, return missing character 
def missing_alpha(st):
    letter = "abcdefghijklmnopqrstvuwxyz" #create total a-z string

    start = letter.index(st[0])          #find out 1 char of string index in letter 
    finish = letter.index(st[len(st)-1]) #find out last char of string index in letter 
    letter = letter[start:finish+1]      #slice string 
    string = ""                          # variable for missing number 
    
    for i in letter:                     # iterate for loop  with char of letter 
        if i not in st:                  # check letter of char is in string 
            string += i                  # add missing number 
    return string       
                     # return missing char
st = input("Enter letters : ")

print(f"Missing Letters in string {st} : ",missing_alpha(st))