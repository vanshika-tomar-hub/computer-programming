# 13. Create a dictionary of keys a, b, and c

# Sample Output

# Dictionary = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                           'Y' : [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#                           'Z' : [21, 22, 23, 24, 25, 26, 27, 28, 29, 30] }

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Z = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

from pprint import pprint
num = dict(A=list(range(1, 11)), Y=list(range(11, 21)), Z=list(range(21, 31)))
pprint(num)
 
for k,v in num.items():
   print(k, " = ", v)

