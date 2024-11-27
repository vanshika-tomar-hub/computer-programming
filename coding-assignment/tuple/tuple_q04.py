# 4. Write a Python program to unpack a tuple in several variables

# Sample Output

# a = 4, 8, 3

# (4, 8, 3)

a = 4, 8, 3 
print(a)
n1, n2, n3 = a
#unpack a tuple in variables
print(n1 + n2 + n3) 
#variables must be equal to the number of items 0
n1, n2, n3, n4= a 
