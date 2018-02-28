try:
	print("try...")
	r = 10 / 0
#print不执行
	print("result:", r)
#捕获分母为零错误
except ZeroDivisionError as e:
	print('except:', e)
#没有异常时执行
else：
	print("no error...")
#不管是否捕获异常，均执行
finally:
	print("finally..")
print("END")
#使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
    	#将错误信息记录到logging文件，异常依然会被抛出
        logging.exception(e)

main()
print('END')


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        #捕获异常后再抛出
        raise
