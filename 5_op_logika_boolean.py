#operasi logika dan boolean

#not or and xor


#NOT
from operator import truediv


print ('===not===')
a=False
c=not a
# print('Data a =', a)
print('Data c =', c)

# OR
print ('==OR==')
a=False
b=False
c=a or b
print('Hasil OR =', c)

# AND
print ('==AND==')
a=False
b=True
c=a and b
print('Hasil AND =', c)

# XOR
print('==XOR==')
a=True
b=False
c=a ^ b
print('Hasil XOR =',c)