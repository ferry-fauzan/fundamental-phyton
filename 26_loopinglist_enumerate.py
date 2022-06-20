kumpulan_angka=[5,2,3,5,7,3,5]

#for loop
print('================')
for angka in kumpulan_angka:
    print(f'Angka: {angka}')

peserta=['Adi','Raka','Fauzan','Samisari','Otong']
for nama in peserta:
    print(f'Nama-nama peserta: {nama}')
print('================\n')

#while
kumpulan_angka=[5,2,3,5,7,3,5]
panjang=len(kumpulan_angka)
i=0

while i < panjang:
    print(f'angka={kumpulan_angka[i]}')
    i+=1

#list comprehension
print(f'\nlist comprehension')
kumpulan_list=['Andara','Kabul',1,4,'Cece',3]
[print (f'Isi list: {kmpl}') for kmpl in kumpulan_list]


#enumarated
print('\nEnumerate')
data_list=['Andara','Kabul',1,4,'Cece',3]

for index,data in enumerate (data_list):
    print(f'Index: {index}, Data: {data}')

