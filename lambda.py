def mul(x):
    return (x * x)


def add(x):
    return (x + x)


fun = [mul, add]
for i in range(5):
    v = list(map(lambda x: x(i), fun))
    print(v)


from functools import reduce

x = [12,23,45,6,587,9,765,4]
a = list(map(lambda i : x[i],range(1,len(x),2)))
b = list(filter(lambda i:i%2==1 and i>0,a))
d = reduce(lambda i,j:i+j,b)
print(d)



