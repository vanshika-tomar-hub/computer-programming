# 8. Write a Python program to count the occurrences of each word in a given sentence

# Sample Output

# string = To change the overall look your document. To change the look available in the gallery

# { 'To': 2, 'change': 2, 'the': 3, 'overall': 1, 'look': 2, 'your': 1, 'document.': 1, 'available': 1, 'in': 1, 'gallery': 1 }

str = "To change the overall look your document. To change the look available in the gallery"
c = dict()
txt = str.split(" ")
for t in txt:
	if t in c:
		c[t] += 1
	else:
		c[t] = 1
print(c)
