# Author:Ligb
"""从OOP模块导入类"""
# 在一个模块中可存储多个类
# 并可以同时导入多个类
# 或者可以导入整个模块 如 import OOP 需要使用句点表示法来进行调用
# 若某一子类的父类定义在另一模块中，则在继承时需要导入父类否则会报错
# from module_name import *但不推荐使用这种方式
# Python标准库习惯在私有库之前导入，然后空一行导入私有库
# collection模块中的OrderedDict类，与字典一样，但是能实现字典的键值对的保存顺序与输入顺序一致
from collections import OrderedDict

from OOP import Car,Dog


my_new_car = Car("xiali", "small", "2012")
print(my_new_car.get_information())
my_dog = Dog("hello", 18)
my_dog.roll_over()


favorite_languages = OrderedDict()
favorite_languages["lee"] = "python"
favorite_languages["wang"] = "c"
favorite_languages["he"] = "c++"
for name,language in favorite_languages.items():
    print(name + " loves the " + language + "best!")
