# -*- coding:utf-8 -*-

from java.lang import System # Java import
from java.util import ArrayList # Java import

print('Running on Java version: ' + System.getProperty('java.version'))
print('Unix time from Java: ' + str(System.currentTimeMillis()))
list = ArrayList()
list.add('a')
list.add('b')
print('list %s' % str(list))
print('list %s' % str(list.class.getName()))
print(type(list))

# https://www.runoob.com/python3/python3-built-in-functions.html
print(locals()) # 执行 locals() 之后, 返回一个字典, 包含(current scope)当前范围下的局部变量
print(globals())