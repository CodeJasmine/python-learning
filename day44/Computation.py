"""
数学运算
"""

# len(s)
# 返回对象内元素个数
dic = {'a': 1, 'b': 3}
print(len(dic))

# max(iterable,*[, key, default]) 返回最大值
print(max(3, 1, 4, 2, 1))

print(max((), default=0))

di = {'a': 3, 'b': 1, 'c': 4}
print(max(di))

a = [{'name': 'xiaoming', 'age': 18, 'gender': 'male'}, {
    'name': ': xiaohong', 'age': 20, 'gender': 'female'}]
print(max(a, key=lambda x: x['age']))

# 如果已知多个列表，找出列表更长的，使用 max 方法


def max_length(*lst):
    return max(*lst, key=lambda v: len(v))


print(max_length([1, 2, 3], [4, 5, 6, 7], [8]))

# pow(x, y, z=None, /)
# x 为底的 y 次幂，如果 z 给出，取余
print(pow(3, 2, 4))

# round(number[, ndigits])
# 四舍五入，ndigits 代表小数点后保留几位
print(round(10.0222222, 3))

# sum(iterable, /, start=0)
# 求和
a = [1, 4, 2, 3, 1]
print(sum(a))
# #求和的初始值为10
sum(a, 10)

# abs(x, /)
# 求绝对值或复数的模
print(abs(-6))

# divmod(a,b)
# 分别取商和余数
print(divmod(10, 3))

# complex([real[, imag]])
# 创建一个复数
print(complex(1, 2))

# hash(object)
# 返回对象的哈希值


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id=' + self.id + ',name = ' + self.name


xiaoming = Student('001', 'xiaoming')
print(hash(xiaoming))

# id(object)
# 返回对象的内存地址
print(id(xiaoming))
