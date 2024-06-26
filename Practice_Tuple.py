import math
# Tuple

# 튜플은 순서가 지정되고 변경할 수 없는 컬렉션이다.
# 또한 중복 값을 허용함, 튜플 항목은 인덱싱됨 
mytuple = ()
mytuple = ("apple", "banana", "cherry")
result = mytuple[1]

thistuple = "apple", "banana", "cherry", "apple", "cherry"
print(thistuple)

# 항목이 하나인 튜플을 만들려면 항목 뒤에 쉼표를 추가해야 함 아니면 튜플로 인식을 안 함 
single_tuple = ("apple",)
print(single_tuple)
no_tuple = ("apple")
print(no_tuple) 

# 기존 튜플 값은 변경이 안됨 (에러 발생)
# thistuple[1] = "pear"
print(len(thistuple))

# 모든 데이터의 유형이 튜플의 항목이 될 수 있다.
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("appple", 40, True)

print(thistuple[:3])
print(thistuple[1:3])

# 튜플 값을 변경하는 방법
print(thistuple)
y = list(thistuple)
y[1] = "orange"
thistuple = tuple(y)
print(thistuple)

# 튜플 추가 작업
fruits = ("apple", "banana", "grape")
fruits += ("pear", "kiwi")
print(fruits)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# 튜플 패킹
fruits = ("apple", "banana", "grape")

# 튜플 언패킹
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# 열거 사용
fruits = ["apple", "banana", "grape"]
for index, value in enumerate(fruits):
    print(index, value)

# 세트
myset = {"apple", "banana", "cherry"}
print(myset)

numbers = set([1,2,3,1,2,3])
print(numbers)

letters = set("abc")
print(letters)

fruits = {"apple", "banana", "grape"}
if "apple" in fruits:
    print("apple is in the fruits set.")

for x in fruits:
    print(x)

# 세트에 항목 추가
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Union Operation:
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x3 = x1.union(x2)

print(x3)
x3 = x1.intersection (x2)
print(x3)
x3 = x1. difference(x2)
print(x3)

#dictionary

thisdict = {
    "brand" : "salomon",
    "model" : "xa-pro-3d",
    "color" : "black"
}

x = thisdict.get("model")
x = thisdict.keys()
print(x)

for key, value in thisdict.items() :
    print(key, ":", value)

# dictionary 정렬
capitals = {
    "Cambodia":"Phnomphen",
    "Korea":"Seoul",
    "USA":"Washington",
    "China":"Beijing"
}
for key in sorted(capitals.keys()):
    print(key, end=" ")
print("\n")

for i, v in enumerate(["a", "b", "c"]):
    print(i)
    print(v)
"""
def calCircle(r) :
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return (area, circum)

radius = float(input("원의 반지름을 입력하시오: "))

(a, c) = calCircle(radius)
print("원의 넓이는", a, "원의 둘레는", c)
"""
contacts = {
    'Kim':'01012345678',
    'Park':'01012345679',
    'Lee':'0101234580'
}
contacts['Choi'] = '01056781234'
contacts.pop("Kim")
print(contacts)

students = [
    {"이름":"김상훈", "학번":"2020039095", "학점":3.2},
    {"이름":"임성빈", "학번":"2020039096", "학점":4.3},
    {"이름":"곽준빈", "학번":"2020039097", "학점":2.7},
]
i = 0
for student in students:
    print(i+1, "번째 학생의 이름은", student["이름"], "학번은", student["학번"], "학점은", student["학점"],"입니다.")
    i += 1
