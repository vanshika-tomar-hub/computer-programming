# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

# Sample Output

# Before Swap = abc xyz

# After Swap = xyc abz

a = 'abc'
b = 'xyz'
print("Before Swap :",a," ",b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print("After Swap :",a1," ",b1)
