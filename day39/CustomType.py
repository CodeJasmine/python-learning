"""
自定义类型
"""


class Girl(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print('I\'m %s, age: %s' % (self.name, self.age))


sln = Girl('sln', '18')
print(sln.name)
print(sln.age)
sln.shout()

# 修改sln的name
sln.name = 'wususu'
print(sln.name)

# 如果想避免属性 name 被修改，可以将它变为私有变量。改动方法：属性前加 2 个 _ 后，变为私有属性


class GirlFriend(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

# 通过另一个例子，解释如何更优雅地改变某个属性为只读或只写。
# 自定义一个最精简的 Book 类，它继承于系统的根类 object：


class Book(object):
    def __init__(self, name, sale):
        self.__name = name
        self.__sale = sale

# 使用 Python 自带的 property 类，就会优雅地将 name 变为只读的。
    @property
    def name(self):
        return self.__name


a_book = Book('magic_book', 2999)
print(a_book.name)

# 如果使 name 既可读又可写，就再增加一个装饰器 @name.setter。


class Book_two(object):
    def __init__(self, name, sale):
        self.__name = name
        self.__sale = sale

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


a_book = Book_two('magic_book', 3999)
a_book.name = 'magic_book_2.0'
print(a_book.name)
