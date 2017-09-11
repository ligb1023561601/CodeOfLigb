# _*_ coding: utf-8 _*_
# @Time     : 2017/9/10 12:06
# @Author    : Ligb
# @File     : files_exception.py

# 1.从文件中读取数据
# open()中添加需打开的文件名,在当前运行的py文件目录中寻找
# 关键字with在用户不需要访问文件后将其关闭，省的用户还需要手动close（）
# 因读取到文件末尾时会返回一个空字符串，所以用rstrip可以去除此空行

import json

file_name = "pi_digits.txt"
with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 以绝对路径打开文件，r表示取消转义字符
file_path = r"C:\Users\ligb\Desktop\exclude mine\Help.txt"
with open(file_path) as abc:
    context = abc.read()
    print(context)

# 逐行读取文件
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# open返回的文件对象只在with代码块内可用
# 若要在with代码块外边使用度取到的文件对象，需要用列表将各行的内容存入列表中
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

# 读取文本文件时，内容被处理成了字符串，要使用的话按自己需求进行转换
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()     # 去除每行末尾的空字符
print(pi_string)

# 2.写入文件
# 若写入的文件不存在，则会创建它；但若已经存在则注意‘W’会清空原来的内容再写入，用附加模式可行
# 写入的内容只能是字符串，故其他格式需经过str（）
# 写入多个行时，需要手动添加换行符\n

filename = "programming.txt"
with open(filename,"w") as file_object:
    file_object.write("这是第一个写入测试！\n")
    file_object.write("这是第二个写入测试！\n")

# 以附加模式对文件进行写入
with open(filename,"a") as file_object:
    file_object.write("这是第三个写入测试！\n")

# 3.异常
# 在有的情况下可以使用pass语句来忽略掉异常，或是用其作为占位符
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("数字正确！")

try:
    with open("hello.txt") as txt:
        contents = txt.read()
except FileNotFoundError:
    print("hello.txt文件不存在！ ")
else:
    print(contents.rstrip())

# 4.存储数据
# 使用模块json存储数据，可以在程序运行时加载数据并且可以与其他程序分享
# 导入整个json模块，用句点表示法调用
# dump()存储数据，load()加载数据
numbers = [2, 3, 6, 8, 7, 9]
data_file = "numbers.json"
with open(data_file,"w") as datas:
    json.dump(numbers,datas)
with open(data_file) as datas:
    rec_data = json.load(datas)
print(rec_data)