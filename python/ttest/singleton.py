# 定义一个元类，它在创建类时会检查是否已经存在实例，如果存在则返回实例，否则创建新的实例
class SingletonMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._instance = None  # 初始化实例为None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:  # 如果实例不存在
            cls._instance = super().__call__(*args, **kwargs)  # 调用父类的__call__方法创建实例
        return cls._instance  # 返回实例


# 使用SingletonMeta作为元类创建一个名为Foo的类，它有一个name属性
class Foo(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name


# 创建Foo的两个对象，并打印它们的id和name
foo1 = Foo("foo1")
foo2 = Foo("foo2")
print(id(foo1), foo1.name)
print(id(foo2), foo2.name)
# 输出：140192518837616 foo1
# 输出：140192518837616 foo1

# 可以看到，foo1和foo2是同一个对象，它们的id和name都相同

'''
首先，定义了一个元类SingletonMeta，它继承自type，也就是默认的元类。
然后，在元类的__init__方法中，给每个类添加了一个_instance属性，用来保存类的实例对象，并初始化为None。
接着，在元类的__call__方法中，重写了类的调用行为，也就是创建对象的行为。 这个方法会检查类的_instance属性是否为None，如果是，则调用父类的__call__方法创建一个新的实例，并赋值给_instance属性；如果不是，则直接返回_instance属性。
最后，使用SingletonMeta作为元类创建了一个名为Foo的类，它有一个name属性。 当我们尝试创建Foo的两个对象时，由于元类的__call__方法的控制，我们只能得到同一个对象，它们的id和name都相同。
这样，我们就实现了单例模式，让Foo类只能有一个实例对象。

Received message. 当然可以。代码的逻辑是这样的： - 首先，定义了一个元类SingletonMeta，它继承自type，也就是默认的元类。 - 然后，在元类的__init__方法中，给每个类添加了一个_instance属性，用来保存类的实例对象，并初始化为None。 - 接着，在元类的__call__方法中，重写了类的调用行为，也就是创建对象的行为。 这个方法会检查类的_instance属性是否为None，如果是，则调用父类的__call__方法创建一个新的实例，并赋值给_instance属性；如果不是，则直接返回_instance属性。 - 最后，使用SingletonMeta作为元类创建了一个名为Foo的类，它有一个name属性。 当我们尝试创建Foo的两个对象时，由于元类的__call__方法的控制，我们只能得到同一个对象，它们的id和name都相同。 这样，我们就实现了单例模式，让Foo类只能有一个实例对象。
'''
