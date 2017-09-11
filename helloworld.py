message = "hello my world!"
print(message)
message = "123456"
print(message)

name = "wo shi da ge"
print(name.title())

first_name = "Lee"
last_name = "VIP"
full_name = first_name+last_name
print(full_name)

# 列表
bicycles = ["trek", 1, "2", "3"]
print(bicycles)
print(bicycles[0])

# 访问最后一个元素索引为-1，倒数第二个为-2，依次类推
print(bicycles[-1])

# 在列表尾部追加元素
bicycles.append("yamaha")
print(bicycles)

# 在列表插入元素
bicycles.insert(0, "hahaha")
print(bicycles)

# 在列表删除元素
# 1.del语句进行删除，删除后就不再存在
del bicycles[2]
print(bicycles)
# 2.pop方法进行删除，删除后返回被弹出的值，可存储至别的变量，不带形参的话默认从尾部弹出
bicycles.pop(2)
print(bicycles)
# 3.根据值来删除元素,但注意只删除一次，若有多个匹配值则需循环删除
bicycles.remove("3")
print(bicycles)

# 组织列表
numbers = [5, 2, 3, 6, 1, 4, 7]
# 1.sort方法永久排序,正向和反向
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# 2.sorted进行临时排序
print(sorted(numbers))
print(numbers)
print(sorted(numbers, reverse=True))

# 确定列表的长度
print(len(numbers))

# 遍历整个列表,in关键字应用很广循环判断语句都行
names = ["lee", "wang", "he"]
for one_name in names:
    print(one_name)

# 数值列表
# 函数range（）的使用
for values in range(1, 5):
    print(values)
# range（）生成以2为步长的数值列表
numbers = list(range(1, 9, 2))
print(numbers)
# 对数字列表进行简单的统计计算
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 列表解析,简化表达式，列表名 = [表达式 for循环取值]
squares = [value**2 for value in range(1, 11)]
print(squares)

# 使用列表的一部分——切片
players = ["Mark", "Mike", "Rose", "Time", "Jin"]
print(players[0:3])
print(players[2:4])
# 若省略起始或结尾的索引，则默认从0与末尾开始；若为负数索引，则为从尾部倒着往回数
print(players[:3])
print(players[4:])
# 复制列表时，用切片进行复制，可以得到两个不同的列表，若直接复制列表名，那么二者指向同一列表
new_players = players[:]
new_players.append("123")
print(new_players)
print(players)

# 元组：类似于列表，但只能储存不可修改的数据集
# 1.任何尝试修改元组元素的操作都会返回类型错误信息
# 2.依旧可以用for循环来遍历元组
dimensions = (200, 50)
print(dimensions[0])
# 3.可以通过重新定义元组的方式对元组进行修改
dimensions = (400, 10)
print("modified dimensions："+str(dimensions))

# if语句
# 用and表示与or表示或，非空字符串被解读为True；if not语句
cars = ["audi", "bents", "bwm", "toyota"]
for car in cars:
    if car == "bwm":
        print(car.upper())
    else:
        print(car.lower())
if cars[0] != "bwm":
    print("This car is not Audi！")
# 用in检查特定值是否包含在列表中，not in 检查特定值不在列表中
if "bents" in cars:
    print("There is a Benz!")
elif "byd" not in cars:
    print("There is no such car!")
else:
    print("hahha")
# 确定列表是不是空的可以将列表名放入if语句，若不为空将返回一个true值

# 字典： 一系列的键-值对,其值可以为任意的数据类型;键-值对的排列顺序并不重要，重要的是其一一对应关系
alien = {"color": "green", "points": 5}
print(alien["color"])
# 在字典中添加键-值对
alien["x_position"] = 10
alien["y_position"] = 100
print(alien)
# 一种常用的字典用法是，先创建一个空的字典，然后根据需求慢慢添加键-值对
# alien = {}
# 修改键-值对
alien["x_position"] = 100
print(alien)
# 删除键-值对,永久删除
del alien["color"]
print(alien)
# 遍历字典
# 1.遍历所有键值对
for key,val in alien.items():
    print("键是：" + str(key) + " " + "值是：" + str(val))
# 2.遍历所有键,若省略keys()，输出将不变，但显式方法更易于理解，该方法返回一个包含所有键的列表；可以sorted（）进行排序
for key in alien.keys():
    print("The key is:" + key)
# 3.遍历所有值，可以用set（)即集合的方式来剔除其中的重复项
for val in set(alien.values()):
    print("The value is:" + str(val))

# 嵌套：在字典中装入列表或者在列表中装入字典;或者在字典中存储字典

# 用户输入与while循环
# 1.函数input（）的工作原理,返回的是一个字符串;在Python2.7中，用的是raw_input()
# message = input("please input something and I wil repeat it back to you:")
# print(message)
# 2.若要输入数值，则使用int（）来获取
age = "22"
age = int(age)
if age >= 18:
    print("I am an adult!")
# 3.while循环,break打断循环，continue
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
while current_number < 7:
    current_number -= 1
    if current_number == 3:
        break
# 4.使用while循环来处理列表和字典
# 在两个列表间进行传递值
# 删除包含特定值的所有列表元素,删除列表中的多个相同的元素，循环remove（）

# 函数
# 1.定义


def greet_user(username):
    """显示简单的问候（此处是注释）"""
    print("hello!" + username)
# 2.函数时关键字实参，位置实参，默认值可以混合使用
greet_user("ligb")
# 关键字实参:是传递给函数的名称-值对，可以结构清晰的避免混淆;并且这样可以不用考虑形参的顺序问题
greet_user(username="lee")
# 在定义函数的时候，可以给每个形参指定默认值，这样可以简化函数调用，并可以实现类似于方法重载的效果
# 若想让实参称为可选的，那么可将该形参指定一个空字符串即可
# 应将有默认值的形参置于靠后的位置，以避免混淆


def describe_pet(pet_type, pet_name="he"):
    print("pet type is:" + pet_type)
    print("pet name is:" + pet_name)
describe_pet("dog",pet_name="www")
# 3.返回值，可返回任何类型的值，返回字典等等


def get_formatted_name(xing, ming):
    entire_name = xing + ming
    return entire_name
print(get_formatted_name("lee", "guibin"))
# 传递列表,并可在函数中进行修改


def greet_users_again(people_names):
    for people_name in people_names:
        print("hello," + people_name.title())
user_names = ["lee", "wang", "he"]
greet_users_again(user_names)

# 4.若想对列表进行操作而又不想影响其中的元素，可以在传递时传递列表的副本而不是原件
# 即切片表示法，如function_name(list_name[:])这种格式表示了创建了该列表的副本，可在函数中传递又不影响原列表
# 不过在非必要的时候并不提倡这种做法，应为会降低效率

# 5.传递任意数量的实参
# 形参名前带上*是为了创建一个空的元组，并可以将收到的任意多个实参封装到这个元组中,即使为也行


def make_pizza(*toppings):
    print(toppings)
make_pizza("pepper")
make_pizza("pepper", "mushrooms", "cheese")
make_pizza()
# 结合使用位置实参和任意数量实参
# 若需要接受任意数量的实参，并且有若干个变量，那么任意数量的形参必须放在最后
# 如 def make_pizza(size,*toppings)
# 使用任意数量的关键字实参,两个**代表创建了一个名叫user_info的字典，然后将收到的所有键值对存入该字典


def build_profile(first, last, **user_info):
    """创建一个字典其中包含用户的所有信息"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key_man, val_man in user_info.items():
        profile[key_man] = val_man
    return profile
user_profile = build_profile("lee", "guibin", address="beijing", ID=11 )
print(user_profile)

