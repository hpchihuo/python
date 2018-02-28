import functools

def log(func):
    @functools.wraps(func)#不会改变func函数名
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
	print("hello world")

log(now)

#带参数装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

log('name')(func)

@log('name')
def now():
	print("hello world")


def metric(fn):
    @functools.wraps(fn)
    def f(*args, **kws):
        start_time = time.time()
        n = fast(*args, **kws)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, start_time-end_time))
        return n
    return f
#使用装饰器后返回的是函数f，但是函数名仍然是fast
@metric
def fast(x, y):
    return x + y 

fast(10, 20)
#调用fast函数，相当于调用了f函数，开始执行，获取时间，获取fast返回值
#若直接返回fast函数，则fast函数没有值接收