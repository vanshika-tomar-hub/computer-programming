# 17. Write a Python program to add a prefix text to all of the lines in a string.

# Sample Output

# Text :
#               Python is an interpreted, object-oriented, high-level programming language
#               that can be used for a wide variety of applications. Python is a powerful
#               general-purpose programming language.

# Prefix to add to each line = *

# Display the Result :

#       *  Python is an interpreted, object-oriented, high-level programming language
#       *  that can be used for a wide variety of applications. Python is a powerful
#       *  general-purpose programming language.

import textwrap
para = """
	Python is an interpreted, object-oriented programming languages. 
	high-level programming language that can be used for a wide variety of applications. 
	Python is a powerful general-purpose programming language.
	First developed in the late 1980s by Guido van Rossum. 
	Python is open source programming language.
	Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
"""
without_Indent = textwrap.dedent(para)
txt = textwrap.fill(without_Indent, width=70)
res = textwrap.indent(txt, '* ')
print(res)
