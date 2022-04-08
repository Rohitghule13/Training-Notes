# function for making staring into camelcase
def Camel_case(st): 
    spacing_char = "/-+=_" # speacial character variable for reference 
    
    for i in st: # loop for removing special character 
       if i in spacing_char:
           st = st.replace(i," ")
    #print(st)
    st = st.split() # make list 
    st[0] = st[0].lower() # make lower case first element 
    
    st[1] = st[1].capitalize() 
    return ("".join(st)) # join list element and retured

st = input("Enter string Input : ") # get input from console

print(Camel_case(st)) #call function
