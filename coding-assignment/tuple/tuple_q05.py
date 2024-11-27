# 5. Write a Python program to add an item in a tuple

# Sample Output

# (10, 40, 50, 70, 90)

# add items in list = 20

# (10, 40, 50, 70, 90, 20)

#create a tuple
t = (10,40,50,70,90) 
print(t)
t = t + (20,)
print(t)
#converting the tuple to list
l = list(t) 
#use different ways to add items in list
l.append(30)
t = tuple(l)
print(t)
