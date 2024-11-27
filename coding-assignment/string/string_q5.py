# 5. Write a Python program to remove the nth index character from a nonempty string.

# Sample Output

# Before Remove = Tutor Joes

# Remove character = t

# After Remove = Tuor Joes

def remove_char(str, n):
      a = str[:n] 
      b = str[n+1:]
      return a + b
print(remove_char('Tutor Joes', 2))
print(remove_char('Tutor Joes', 7))

