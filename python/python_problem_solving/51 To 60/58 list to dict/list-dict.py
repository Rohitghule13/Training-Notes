name = ["rohit","rohan","ajay","suhas"]
score = [87,98,86,89]
result = {i:j for i,j in zip(name,score)}
print(result)
result["vaibhav"]= 100
print(result)