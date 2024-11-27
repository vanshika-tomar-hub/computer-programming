# 13. Write a Python program to remove a newline in Python.

# Sample Output

# String = "\nTutor \nJoes \nComputer \nEducation\n"

# Before Remove NewLine(\n)
# Tutor
# Joes
# Computer
# Education

# After Remove NewLine(\n) = Tutor Joes Computer Education

str = "\nTutor \nJoes \nComputer \nEducation\n"
#Before Remove NewLine(\n)
print(str)
#After Remove NewLine(\n)
print(''.join(str.splitlines()))
