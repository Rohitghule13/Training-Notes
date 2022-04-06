def palindrome(num):
    rem = 0
    summ = 0
    while(num>0):
        rem = num%10
        summ = (summ*10)+rem
        num = num//10
    #print(summ)
    return summ
num = int(input("Enter the number : "))
if palindrome(num)==num:
    print("This is palindrom Number! ")
else:
    print("This is not palindrome number!")