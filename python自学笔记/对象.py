# -*- coding: utf-8 -*-
#在class中定义私有属性，self.__name = name,只能通过类内部方法访问，也可以_className__name访问
#多态，如果一个类继承于某一个类，则可将该类看做为父类类型，isinstnce()返回True，
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。 
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
#类属性与实例属性，实例对象均可访问，优先访问实例属性
from types import MethodType


class Student(object):
	pass

s = Student()
#动态给类添加一个属性
s.name = 'hepan'

def set_age(self,age):
	self.age = age
#给实例绑定一个方法，只对该实例起作用
s.set_age = MethodType(set_age,s)

def set_score(self, score):
   	self.score = score
#给类绑定方法后，所有实例均可使用
Student.set_score = set_score

#可以用__slot__限制实例属性,对子类不起作用
class Student(object):
	__slots__ = ('name', 'age')

class Screen(object):
    @property#对应get方法
    def width(self):
        return self._width
    @width.setter#对应set方法
    def width(self,value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width*self.height

S = Screen()
S.width = 1024 #通过装饰器调用了set方法
S.width #通过装饰器调用了get方法

#若只有property，则只能获取


#多重继承：通过多重继承，一个子类就可以同时获得多个父类的所有功能。



#定制类
class Student(object):
    def __init__(self, name):
        self.name = name
#使用print(Student('hepan'))时，会自动调用__str__方法
    def __str__(self):
        return 'Student object (name: %s)' % self.name
#s = Student('name'), s 会调用__repr__方法
    __repr__ = __str__


#__iter__ :如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration
		return self.a
	#可以通过下标访问,也可以切片访问
	def __getitem__(self, n):
		if isinstance(n,int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b
			return L

f = Fib()
f[124]

for n in Fib():
	print(n)


#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法
#当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
#__call__:任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。


#，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：


from enum import Enum,unique

#保证不重复
@unique()
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

#class名为‘Hello',继承于object，创建了一个方法hello
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class


#metaclass：先定义metaclass，就可以创建类，最后创建实例。
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：

#     当前准备创建的类的对象；

#     类的名字；

#     类继承的父类集合；

#     类的方法集合。
