# 15. Sort Counter by value

# Sample Output

# Before Sort = { 'Tamil': 92, 'Math' : 88, 'Science' : 89, 'Social' : 89, 'English' : 56 }

# After Sort = ('Tamil', 92), ('Science', 89), ('Social', 89), ('Math', 88), ('English', 56)

from collections import Counter
x = Counter({'Tamil':92, 'Math':88,'Science':89, 'Social':89, 'English':56})
print(x.most_common())
