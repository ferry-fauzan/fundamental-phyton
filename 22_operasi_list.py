from itertools import count


data_angka=[1,2,3,4,4,6,3,4,9]

#count
jumlah_data4=data_angka.count(4)
print(f'Jumlah data  4= {jumlah_data4}')

#ambil posisi
nama=['ferry','fauzan','Hayya']
fauzan_index=nama.index('fauzan')
print(f'Fauzan ada diangka: {fauzan_index}')

#mengurutkan list
data_angka.sort()
print(f'Angka setelah di short {data_angka}')

#urut bawah
data_angka.reverse()
print(f'Angka setelah di short {data_angka}')