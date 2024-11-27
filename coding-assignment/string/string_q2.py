# 2. Write a Python program to count the number of characters (character frequency) in a string.

# Sample Output

# litchi

# {'t' : 2, 'u' : 1, 'o' : 2, 'r' : 1, 'j' : 1, 'e' : 1, 's' : 1}

str ="litchi"
dict = {}
for c in str:
	keys = dict.keys()
	if c in keys:
		dict[c] += 1
	else:
		dict[c] = 1
print(dict)
