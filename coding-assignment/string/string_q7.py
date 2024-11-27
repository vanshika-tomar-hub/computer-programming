# 7. Write a Python program to remove the characters which have odd index values of a given string

# Sample Output

# String = Computer Education

# Remove Odd Index Char = Cmue dcto

str="Computer Education"
res = ""
print("Original String :",str) 
for i in range(len(str)):
	if i % 2 == 0:
	  res = res + str[i]
print("Remove Odd Index Char :",res)
