# -*-coding=utf-8 -*-
# mysql

# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:
conn = mysql.connector.connect(host='192.168.1.115', port=3306, user='root', password='123456', database='test',
                               use_unicode=True)
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print values
[(u'1', u'Michael')]
# 关闭Cursor和Connection:
cursor.close()
conn.close()
