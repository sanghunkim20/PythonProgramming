i = -20
print(abs(i))

f = -30.92
print(abs(f))

mylist = [1,2,3,0]
print(any(mylist))

"""
x=10
print(eval('x+1'))
exp = input("input arithmetic expression :")
print(eval(exp))
"""
s=[1,2,3,4]
print(sum(s))

def square(n):
    return n*n
mylist=[1,2,3,4,5]
result = list(map(square, mylist))
print(result)

seasons = ['봄', '여름', '가을', '겨울']
print(list(enumerate(seasons, start=1)))

def myfilter(x):
    return x>3
result = filter(myfilter, (1,2,3,4,5,6))
print(list(result))

numbers = [ 1 , 2 , 3 , 4 ] 
slist = [ '하나' , '둘' , '셋' , '넷' ] 
print ( list ( zip (numbers, slist)))

print(sorted([4, 2, 3, 5, 1]))  
myList = [4, 2, 3, 5, 1]
myList.sort()
print(myList)

students = [
    ('Hong', 3.9, 20160303),
    ('Kim', 3.0, 20160302),
    ('Choi', 4.3, 20160301)
]
print(sorted(students, key=lambda student:student[0], reverse=True))

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "<Name: %s, Age: %s>" % (self.name, self.age)
def keyName(person):
    return person.name

def keyAge(person):
    return person.age

people = [Person("Hong", 20), Person("Kim", 35), Person("Choi", 38)]
print(sorted(people, key=keyName))

list_a = [ 1, 2, 3, 4, 5 ]
f = lambda x : 2*x
result = map(f, list_a)
print(list(result))

list_a = [1,2,3,4,5,6]
result = filter(lambda x: x%2 == 0, list_a)
print(list(result))

def celsius(T):
    return (5.0/9.0)*(T-32.0)
f_temp = [0, 10, 20, 30, 40, 50]
c_temp = map(celsius, f_temp)
print(list(c_temp))

def myGenerator():
    yield 'first'
    yield 'second'
    yield 'third'

for word in myGenerator():
    print(word)

import sys
import time
import calendar
cal = calendar.month(2024, 6)
print(cal)
