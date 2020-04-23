"""
简单选择排序
"""


def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == '__main__':
    list = [58, 28, 18, 88, 8]
    print(select_sort(list))
