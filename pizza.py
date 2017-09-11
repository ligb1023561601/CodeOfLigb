# Author:Ligb

# 1.导入整个模块
# 将函数存储在模块中import应放在文件开头
# 模块是后缀名为.py的文件，通过import可以导入模块；import实际是在后台将要导入的模块的程序复制进来
# 调用函数时需要用句点
import helloworld
helloworld.make_pizza("pepper")
helloworld.make_pizza("mushrooms", "pepper")

# 2.导入特定的函数,这种做法显式地导入了函数，不再需要句点
from helloworld import make_pizza, greet_user
make_pizza("onions")

# 3.使用as给函数指定别名
from helloworld import make_pizza as mp

# 4.使用as给模块指定别名
import helloworld as hw

# 5.使用*号可以导入模块中的所有函数，显式导入；不建议使用，因为若导入的函数名称与自己的重复，那么会覆盖函数
from helloworld import *