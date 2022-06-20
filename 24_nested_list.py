data1=[1,2,3]
data2=[4,5,6,7]
unidata=[data1,data2]

print(f'Gabungan List: {unidata}')

pst1=['Ferry','Karyawan','26']
pst2=['Fauzan','Penguasaha','25']
pst3=['Chiko','Influencer','25']

list_peserta=[pst1,pst2,pst3]
for peserta in list_peserta:
    print(f'Nama: {peserta[0]}')
    print(f'Pekerjaan: {peserta[1]}')
    print(f'Umur: {peserta[2]}\n')