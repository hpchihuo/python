def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

f1()
f2()
f3()
#均返回9
#返回闭包：返回函数不要引用任何循环变量，或者后续会发生变化的变量。 
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


def createCounter():
    n = 0
    def counter():
        n = n+1
        return n
    return counter
#报错