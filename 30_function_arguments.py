def siswa(nama):
    print (f'Siswa ini bernama: {nama}')

siswa('mario')

#fungsi dengan keywords argumen
def mapel(nama,hari):
    print(f'Bp/Ibu {nama} mengajar di hari {hari}')

mapel('Sugeng','Kamis')
mapel(nama='Sandra',hari='Senin')

#fungsi dengan menggunakan default
def guru(nama,mapel='Math',nik='200'):
    print(f'Bp/Ibu {nama} mengajar mapel {mapel} dengan nik {nik}')

guru('Mamat')
guru('Saiko',mapel='Biology',nik=100)