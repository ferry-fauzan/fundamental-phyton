class mahasiswa():

    jurusan='data sains'
    __nilai=5 #private

    def __init__(self ,input_nama,input_nim):
        self.nama=input_nama    #public
        self.nim=input_nim      #public

    def ujian(self,input_nilai):
        self.__nilai+= input_nilai

    def uas(self, input_nilai):
        self.__nilai+= input_nilai

    def cek_status(self):
        if self.__nilai <=80:
            print(self.nama, 'Tidak Lulus')
        else:
            print(self.nama, 'Lulus')



otong=mahasiswa("Fauzan",2015)
ojan=mahasiswa("Ferry",2015)

otong.ujian(50)
otong.uas(10)
otong.cek_status()

ojan.ujian(80)
ojan.uas(10)
ojan.cek_status()