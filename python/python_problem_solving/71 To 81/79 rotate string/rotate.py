# this Function used for left rotation
def leftRotation(st):
    rotate = []              # rotate list
    for i in range(len(st)): # iterate for loop 
        left1 = st[0:1]      # slice first string char 
        left2 = st[1:]       # left first string slice entire string 
        st = left2+left1     # concate two sliced string 
        rotate.append(st)    # append item in list
    print("Left Rotate : ",rotate)            # Display rotate list
 
# this Function used for Right rotation
def rightRotation(st):
    rotate = []              # rotate list
    for i in range(len(st)): # iterate for loop 
        right1 = st[-1]      # slice last string char 
        right = st[0:-1]     # left last string slice entire string 
        st = right1 + right  # concate two sliced string 
        rotate.append(st)    # append item in list
    print("Right Rotate : ",rotate)            # Display rotate list

st = input("Enter String To Rotate : ")
leftRotation(st)
rightRotation(st)