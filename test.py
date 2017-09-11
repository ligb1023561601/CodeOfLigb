# _*_ coding: utf-8 _*_
# @Time     : 2017/9/10 21:30
# @Author    : Ligb
# @File     : test.py
"""测试代码"""

# python 标准库中的模块unittest提供代码测试工具
# 个人理解：测试代码实际上就是讲写好的代码取实际地使用以下，但是由于是测试用的放在主程序中不简洁，可以专门写一个测试用的
# 类来进行使用

import unittest


def get_formatted_name(first, last, middle=""):
    """generate a neatly formatted full name"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()


class NameTestCase(unittest.TestCase):
    """必须继承TestCase类才能进行检查，命名时最好在上Test这个词
    用方法判断函数运行结果与预期结果是否相同
    并且其中的测试方法必须以test_开头，这样main函数就是自动执行
    该方法"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin", "he")
        self.assertEqual(formatted_name, "Janis He Joplin")

# main()用于运行这个文件中的测试方法
unittest.main()


