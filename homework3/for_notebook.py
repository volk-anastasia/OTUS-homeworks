import numpy as np

a = np.zeros(10)
a[4]=1
print(a)

b = np.arange(10, 50)
b_inverse = np.flip(b)
b_even = []
for i in b_inverse:
    if i % 2 == 0:
        b_even.append(i)

print(b_even)

c = np.arange(9).reshape(3, 3)
print(c)

d = np.random.rand(4,3,2)
print(d)
print(f"MIN = {np.min(d)} \nMAX = {np.max(d)}")

e_1 = np.random.rand(6,4)
e_2 = np.random.rand(4,3)
print(e_1.dot(e_2))