# 6. Write a Python program to change a given string to a new string where the first and last chars have been exchanged

# Sample Output

# Before Exchange = Python

# After Exchange = nythoP

str = "Python"
print("Before Swap :",str)
res = str[-1:] + str[1:-1] + str[:1]
print("After Swap :",res)
