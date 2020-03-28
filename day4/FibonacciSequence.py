"""
生成斐波那契数列的前20个数
"""

i = 0
j = 1
print(j, end='')
for num in range(2, 21):
    z = i + j
    print(',', z, end='')
    i = j
    j = z
print()
