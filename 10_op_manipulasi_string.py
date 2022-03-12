# menyambung string concatenate
nama='ferry'
name='fauzan'

namaku= nama +' ' + name
print(namaku)

#menghitung panjang nama
panjang=(len(namaku))
print('Cara cek panjang str:',str(panjang),type(panjang))

#operator untuk string

#1. cek komp char/string di string

d='f'
status=d in namaku
print('Cara cek str/char dalam str:' ,status)

# mengulang string
d='Ini pengulangan:'
print(d,"wk"*10)

#indexing
print('index ke-1:',namaku[1])
print('index ke 0-5:',namaku[0:6])

#melihat urutan string
print('Melihat urutan paling kecil', min(namaku[1]))
print('Melihat urutan paling besar', max(namaku[2]))

#op dalam bentuk method

data='Junior data scientist'
jumlah=data.count('a')
print('Jumlah a pd string: ',jumlah)