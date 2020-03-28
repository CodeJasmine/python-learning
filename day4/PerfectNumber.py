"""
找出10000内的完美数
"""

for i in range(2, 10001):
    num = 0
    for j in range(1, i):
        if i % j == 0:
            num += j
    if i == num:
        print(i)
print()
