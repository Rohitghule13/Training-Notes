def detect_lower(password):
    for i in range(len(password)):
        if password[i].islower():
            return True
    print("Enter the Upper character at least one")
    return False

def detect_upper(password):
    for i in range(len(password)):
        if password[i].isupper():
            return True
    print("Enter the Upper character at least one")
    return False

def detect_Specialchar(password):
    Special = "~!@#$%^&*?"
    for i in range(len(password)):
        if password[i] in Special:
            return True
    print("Enter The special character !")
    return False 
def detect_alphnum(password):
    if any(i for i in password if i.isalnum()):
        return True
    else:
        return False

print("Enter the password length 7max 3min inlcuding letter upper+lower case, special character and numbers")
password = input("Enter the password : ")
if(len(password) >= 3 and len(password) <= 7):
    if detect_alphnum(password):
        if(detect_Specialchar(password) and detect_lower(password) and detect_upper(password)):
            print("You entered strong password : ",password)
else:
    print("Oops you entered week password try it once ! ")