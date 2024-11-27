# 19. Write a Python program to print the following floating numbers upto 2 decimal places with a sign

# Sample Output

# Floating Point Number1 = -84.99

# Print Number with a sign and two decimal places = -84.99

# Floating Point Number2 = 23.36778

# Print Number with a sign and two decimal places = +23.37
a =-84.99
b = 23.36778
print("Original Value A : ", a)
print("Formatted Value A : "+"{:+.2f}".format(a));
print("Original Value B : ", b)
print("Formatted Value B : "+"{:+.2f}".format(b));

