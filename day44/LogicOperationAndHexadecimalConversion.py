"""
逻辑运算和进制转换
"""

# all(iterable)
# 接受一个迭代器，如果迭代器的所有元素都为真，返回 True，否则返回 False
print(all([1, 0, 3, 6]))
print(all([1, 2, 3]))
print(all([1, 3, 5, 7]))

# any(iterable)
# 接受一个迭代器，如果迭代器里有一个元素为真，返回 True，否则返回 False
print(any([0, 0, 0, []]))
print(any([0, 0, 1]))

# ascii(object)
# 调用对象的 repr() 方法，获得该方法的返回值


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id=' + self.id + ',name = ' + self.name


xiaoming = Student('001', 'xiaoming')
print(xiaoming)
print(ascii(xiaoming))

# bin(x)
# 将十进制转换为二进制
print(bin(10))

# oct(x)
# 将十进制转换为八进制
print(oct(9))

# hex(x)
# 将十进制转换为十六进制
print(hex(15))
