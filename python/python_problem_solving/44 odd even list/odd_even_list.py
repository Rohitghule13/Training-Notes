odd = []
even = []
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28] 
for i in range(1,len(l1),2):
    odd.append(l1[i])
for i in range(0,len(l2),2):
    even.append(l2[i])
print("Odd List : ",odd)
print("Even List : ",even)
print("Joint List : ",odd+even)