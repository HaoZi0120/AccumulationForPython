# -*- coding=utf-8 -*-
# 操作文件和目录
# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

import os

print "os.name=", os.name
print "os.uname()=", os.uname()
print "os.environ=", os.environ
print "os.getenv('PATH')=", os.getenv('PATH')
print
print "os.path.abspath('.')", os.path.abspath('.')
print "os.path.join('far','chi')", os.path.join('far', 'chi')
print "os.path.split('/aaa/bbb/asdf.txt')", os.path.split('/aaa/bbb/asdf.txt')
print "os.path.splitext('/aaa/bbb/asdf.txt')", os.path.splitext('/aaa/bbb/asdf.txt')
print
print "[x for x in os.listdir('.') if os.path.isfile(x)]", [x for x in os.listdir('.') if os.path.isfile(x)]
print "[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']", [x for x in os.listdir('.')
                                                                                              if os.path.isfile(x) and
                                                                                              os.path.splitext(x)[
                                                                                                  1] == '.py']
