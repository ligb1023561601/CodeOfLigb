# Author:Ligb
# 1.定义一个类，规定类名的首字母大写，括号是空的，所以是从空白创建了这个类
# _init_()方法在创建类的新实例的时候就会自动运行，两个下划线是用来与普通方法进行区分
# self是一个自动传递的形参，指向实例本身的引用，在调用方法时，不必去给它传递实参
# 以self作前缀的变量称之为属性
# 命名规则
# object（） 共有方法 public
# __object()__ 系统方法，用户不这样定义
# __object() 全私有，全保护方法 private protected，无法继承调用
# _object() private 常用这个来定义私有方法，不能通过import导入,可被继承调用
# 两种私有元素会被转换成长格式（公有的），称之为私有变量矫直，如类A有一私有变量__private,将会被转换成
# _A__private作为其公有变量，可以被继承下去


class Dog(object):

    def __init__(self, name, age):
        """初始化属性name与age"""
        self.name = name
        self.age = age

    def sit(self):
        """类中的函数称为方法"""
        print(self.name.title() + " is now sitting!.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog("he", 2)
my_dog.sit()
my_dog.roll_over()


class Car(object):
    """创建一个汽车类"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 属性具有默认值

    def _get_information(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def update_info(self,date):
        """通过方法修改属性"""
        self.year = date

    def increment_info(self,miles):
        """通过方法进行属性递增"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car's gas tank is full!")

my_car = Car("audi", "big", "1993")
my_car_info = my_car._get_information()
print(my_car_info)

# 2.给属性指定默认值
# 3.三种方法进行修改：通过实例修改，通过方法进行设置，通过方法进行递增（类似于方法进行设置）
my_car.model = "small"

# 4.继承
# 在括号中的类称为父类，super（）函数可以令子类包含父类的所有实例
# 在Python2.7中，继承语法为
# super（Electric_Car,self)._init_(make,model,year)
# 5.重写父类中的方法，可实现多态，父类中的方法将被忽略，包括init方法，若子类不写，则用父类的init方法


class Battery(object):
    """将电动车的电池相关属性提取出来"""
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_mileage(self):
        """显示行驶里程"""
        if self.battery_size == 70:
            mileage = 240
        elif self.battery_size == 85:
            mileage = 270

        message = "This car can go approxiamately " + str(mileage)
        message += "miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类属性,并定义电动车独有的属性"""
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def fill_gas_tank(self):
        print("Electric Cars do not have a gas tank!")

my_tesla = ElectricCar("Tesla", "medium","2017")
print(my_tesla._get_information())
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_mileage()

# 6.将实例用作属性,将类中某些相近的属性再疯封装成小类，然后将这些小类实例化后作为大类的属性，以达到更清晰的结构
# 7.导入类:实现代码的简洁原则，内容在my_car.py中




