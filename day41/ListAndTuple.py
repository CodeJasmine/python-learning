"""
list 和 tuple 的 13 个经典使用案例
"""

from random import randint, sample
from random import shuffle
from random import uniform
from pyecharts.charts import Scatter
import pyecharts.options as opts

#  判断 list 内有无重复元素
# 使用 list 封装的 count 方法，依次判断每个元素 x 在 list 内的出现次数。
# 如果大于 1，则立即返回 True，表示有重复。
# 如果完成遍历后，函数没返回，表明 list 内没有重复元素，返回 False。


def is_duplicated(lst):
    for x in lst:
        if lst.count(x) > 1:
            return True
    return False


a = [1, -2, 3, 4, 1, 2]
print(is_duplicated(a))

# 以上方法实现不简洁，借助 set 判断更方便：


def is_duplicated_two(lst):
    return len(lst) != len(set(lst))

# 列表反转


def reverse(lst):
    return lst[::-1]


r = reverse([1, -2, 3, 4, 1, 2])
print(r)

# 找出列表中的所有重复元素


def find_duplicate(lst):
    ret = []
    for x in lst:
        if lst.count(x) > 1 and x not in ret:
            ret.append(x)
    return ret


ra = find_duplicate([1, 2, 3, 4, 3, 2])
print(ra)

# 斐波那契数列
# 普通实现版本


def fibonacci(n):
    if n <= 1:
        return [1]
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib


r = fibonacci(10)
print(r)
# 生成器版本


def fibonacci_two(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci_two(1)))

# 出镜最多


def mode(lst):
    if lst is None or len(lst) == 0:
        return None
    return max(lst, key=lambda v: lst.count(v))


lst = [1, 3, 3, 2, 1, 1, 2]
r = mode(lst)
print(f'{lst} 中出现次数最多的元素为:{r}')
# 返回多个


def mode_two(lst):
    if lst is None or len(lst) == 0:
        return None
    max_freq_elem = max(lst, key=lambda v: lst.count(v))
    max_freq = lst.count(max_freq_elem)  # 出现最多次数
    ret = []
    for i in lst:
        if i not in ret and lst.count(i) == max_freq:
            ret.append(i)
    return ret


print(mode_two([1, 1, 2, 2, 3, 2, 1]))

#  更长列表


def max_len(*lists):
    return max(*lists, key=lambda v: len(v))


r = max_len([1, 2, 3], [4, 5, 6, 7], [8])
print(f' 更长的列表是 {r}')

# 求表头


def head(lst):
    return lst[0] if len(lst) > 0 else None


print(head([]))
print(head([3, 4, 1]))

# 求表尾


def tail(lst):
    return lst[-1] if len(lst) > 0 else None


print(tail([]))
print(tail([3, 4, 1]))

# 打印乘法表


def mul_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(j) + str("*") + str(i)+"=" + str(i*j), end="\t")
        print()


mul_table()

# 元素对


def pair(t):
    return list(zip(t[:-1], t[1:]))


pair([1, 2, 3])
pair(range(10))

# 样本抽样
lst = [randint(0, 50) for _ in range(100)]
print(lst[:5])
lst_sample = sample(lst, 10)
print(lst_sample)

# 重洗数据集
lst = [randint(0, 50) for _ in range(100)]
shuffle(lst)
print(lst[:5])

# 生成满足均匀分布的坐标点


def draw_uniform_points():
    x, y = [i for i in range(100)], [round(uniform(0, 10), 2)
                                     for _ in range(100)]
    print(y)
    c = (Scatter()
         .add_xaxis(x)
         .add_yaxis('y', y))
    c.render()


if __name__ == '__main__':
    draw_uniform_points()
