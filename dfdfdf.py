a = ['2','4','141']
b = ['pizda','huy','lala']
c = []
a = a*10
print(a)
print('msa',a[2][1])
a[2] = b
print(a)
print('mas',a[2][2])
c.append(a)
c.append(b)
print(c)
print(c[1][0])
f = ['']
f = f*10
print('blya',f)
d = [[]]
d = d*10
print (d)
d[0] = b
d[5] = a
print(d)
