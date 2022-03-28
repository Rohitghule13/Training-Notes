def Hours_to_sec(x):

    minutes = x*60   #it convert hours into minutes
    second  = minutes*60  #it convert minutes into sec
    return second    #return second from hours

try:
    x = int(input("Enter the hours in number"))
    print(Hours_to_sec(x))
except BaseException:
    print("somthing went wrong please enter the hours in number only")


