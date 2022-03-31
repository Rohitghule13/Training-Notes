def exception_handling(a):
    print("result : ",5/a)
try:
    a = 0
    exception_handling(a)
except ZeroDivisionError as e:
    print("this is zero divisible error : ",e)
