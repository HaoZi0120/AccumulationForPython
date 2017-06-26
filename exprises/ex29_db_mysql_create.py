# -*-coding=utf-8 -*-
# mysql

# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:

conn = mysql.connector.connect(host='192.168.1.115', port=3306, user='xmh', password='222222', database='test',
                               use_unicode=True)
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()
conn.close()
