# -*- coding=utf-8 -*-
#文件读写

with open('./ex19_wenjianduxie.py','r') as f :
    print f.read()

import codecs
with codecs.open('./ex19_wenjianduxie.py','r','utf-8') as f:
    print f.read()