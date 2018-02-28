assert n != 0, 'n is zero!'
#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

#如果断言失败，assert语句本身就会抛出AssertionError(n is zero)

#通过pdb调试代码
#python -m pdb err.py
pdb.set_trace()#设置断点，暂停进入调试环境



#将错误输出到日志文件中
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)