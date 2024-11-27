# 7.Write a Python script to print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of keys.

# Sample Output

# Enter the Limit : 5

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


l=int(input("Enter the Limit : "))
d = dict()
for x in range(1,l+1):
    d[x]=x**2
print(d)
