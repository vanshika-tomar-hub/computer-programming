# 18. Write a Python program to flatten a shallow list

# Sample Output

# [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]

# [20, 30, 70, 30, 90, 10, 30, 20, 70, 90, 10, 80]

import itertools
ori_list = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
merged_list = list(itertools.chain(*ori_list))
print(merged_list)
