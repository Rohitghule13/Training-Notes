def check_sentence(st):
    #digit = "1234567890"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    count_letter = 0 
    count_upper = 0 
    count_digit = 0 
    count_lower = 0 
    for i in st:
        if i in upper:
            count_letter += 1 
            count_upper += 1 
        elif i in lower:
            count_letter += 1 
            count_lower += 1 
        else:
            count_digit +=1 
            
    print("Letter in sentence : ",count_letter)
    print("Upper case in sentence : ",count_upper)
    print("Lower case in sentence : ",count_lower)
    print("Digit in sentence : ",count_digit)

st = input("Enter Sentence Here : ")
check_sentence(st)