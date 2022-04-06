date1 = list(map(int,input("Enter date 1 : ").split()))
date2 = list(map(int,input("Enter date 2 : ").split()))
if(date1[0]!=date2[0]or date1[1]!=date2[1]or date1[2]!=date2[2]):
    date = ((date2[0]-date1[0])*360)+((date2[1]-date1[1])*30)+((date2[2]-date1[2]))
    print(f"Days Between two date is {date}!")
else:
    print("Days Between two date is 0!")