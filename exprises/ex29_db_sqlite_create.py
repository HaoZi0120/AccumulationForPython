# -*-coding=utf-8 -*-
# sqlite数据库

# 导入SQLite驱动:
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('ex_29_test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
cursor.rowcount
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
