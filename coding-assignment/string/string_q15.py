# 15. Write a Python program to display formatted text (width=35,70) as output.

# Sample Output

# Python is an interpreted, object-oriented, high-level programming language
# that can be used for a wide variety of applications. Python is a powerful
# general-purpose programming language.

# Formatted Text (Width 35) :
# Python is an interpreted, object-
# oriented, high-level programming
# language that can be used for a
# wide variety of applications.
# Python is a powerful general-purpose
# programming language.

# Formatted Text (Width 70) :
# Python is an interpreted, object-oriented, high-level programming language
# that can be used for a wide variety of applications. Python is a powerful
# general-purpose programming language.

import textwrap
para = """
Python is an interpreted, object-oriented, high-level programming language that can be used for a wide variety of applications. Python is a powerful general-purpose programming language. First developed in the late 1980s by Guido van Rossum. Python is open source programming language. Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
"""
print(textwrap.fill(para, width=35))
print("\n\n",textwrap.fill(para, width=70))
