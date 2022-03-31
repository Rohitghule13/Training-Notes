try:
    deposit = list(map(int,input("space separted deposit ammount : ").split()))
    withdrawal = list(map(int,input("space separted deposit ammount : ").split()))
    print("Your remaining amount : ",sum(deposit)-sum(withdrawal))
except BaseException:
    print("somthing went wrong please enter ammount in integer ")