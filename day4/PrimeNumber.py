"""
输出100以内所有的素数
"""

j = 2
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            j += 1
    if j == i:
        print(i, '', end='')
print()
