# transcrypt hello.py
# transcrypt -n hello.py // no minification
print('Hello world!')
l=list([1, 2, 3])
l.append(4)
l.remove(1)
print(l)
print(l == list)
print('typeof l', type(l))
t=(1, 2)
print(t)

def add(num1, num2):
    return num1 + num2

print(add(2, 3))
print(type(1))
print(type(1.0))