def abstract_num(x):
    if x < 0:
        return -x
    else:
        return x
    
a = 3
b = 5
print(abstract_num(a-b))

def plus_ten(x):
    x = x + 10
    print(x)
    return x + 10

x = 20
print(x)
y = plus_ten(x)
print(x)
print(y)

def pow_num(x, y):
    return x ** y

print(pow_num(2, 10)) 