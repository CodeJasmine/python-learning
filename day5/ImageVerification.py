"""
判断传入的文件名是否为图片类型的文件
"""


def picture(file):
    if file.endswith('png') or file.endswith('jpg') or \
            file.endswith('webp') or file.endswith('bmp') or file.endswith('jpeg'):
        print(this_file, '是图片文件')
    else:
        print(this_file, '不是图片文件')


this_file = input('请输入要上传的文件：')
picture(this_file)
