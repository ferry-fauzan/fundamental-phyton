# method adalah fungsi yg menempel pada class   

class mahasiswa():
    nama='nama' #template

    def belajar(self, mapel):
        print(f'{self.nama} sedang Belajar {mapel}')

    def makan(self):
        print(f'{self.nama} lagi makan siang')

# main program
zain=mahasiswa()
otong=mahasiswa()

otong.nama='otong surotong'

print(zain.nama)
print(otong.nama)

zain.belajar('statistik')
otong.makan()