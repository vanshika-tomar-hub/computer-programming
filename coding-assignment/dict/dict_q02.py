#  Write a Python program to add a key to a dictionary

# Sample Output

# dictionary = {"Name" : "Ram" , "Age" : 23}

# add_key = {"City" : "Salem"}

# dictionary = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem'}

d = {"Name":"Ram" , "Age":23}
print(d)
d.update({"City":"Salem"})
print(d)
d["Gender"]="Male"
print(d)


