#stack

tumpukan=[1,2,4,5]
print(f'data awal {tumpukan}')
#memasukkan data baru
tumpukan.append(9)
print(f'data append {tumpukan}')

#hilangkan data dr belakang
tumpukan.pop()
print(f'data pop {tumpukan}')

#queue
from collections import deque
print('\n',38*'=')
antrian=deque([2,4,6,4])

print('data sekarang: ', antrian)

#menambahkan data
antrian.append(8)
print(f'Data Masuk 8')
print(f'Data : {antrian}')

#mengurangi antrians

i=0
while i <= 6:
    i+=1
    out=antrian.popleft()
    print(f'Data Keluar: {out}')
    print(f'Data : {antrian}')
