#class
class mahasiswa():

    # jurusan='ekonomi'

    jumlah_mahasiswa=0

    def __init__ (self,input_nama,input_nim):
        self.nama= input_nama # public
        self.nim=input_nim # public
        mahasiswa.jumlah_mahasiswa+=1

#main program
ojan=mahasiswa('fauzan',25)
aji=mahasiswa('Parama',66)

print(mahasiswa.jumlah_mahasiswa)

# mahasiswa.jurusan='ekonomi mikro'
# ojan.jurusan='data sains'

# print(mahasiswa.jurusan)
# print(ojan.jurusan)
# print(aji.jurusan)

# print(mahasiswa.__dict__)
# print(ojan.__dict__)
# print(aji.__dict__)