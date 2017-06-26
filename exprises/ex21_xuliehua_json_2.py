# -*- coding=utf-8 -*-
# 序列化

import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def temp(self):
        print self.name


s = Student('Bob', 20, 88)
print 's.__dict__', s.__dict__


# print(json.dumps(s))

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s_j = json.dumps(s, default=student2dict)

s_j = json.dumps(s, default=lambda obj: obj.__dict__)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s_o = json.loads(s_j, object_hook=dict2student)
print s_o
