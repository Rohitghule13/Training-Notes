num = int(input("Enter the Number : "))
num1 = num
num = str(num)
num = num.replace(""," ")
num = num.split()
num = reversed(num)
num = "".join(num)
num = int(num)
if num1==num:
    print("This is palindrome Number ! ")
else:
    print("This is not palindrome Number ! ")