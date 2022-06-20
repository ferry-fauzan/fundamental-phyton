#belajar turunan

class Ojek():
    def __init__(self, nama, motor, area):
        self.nama=nama
        self.motor=motor
        self.area=area

    def cek_id(self):
        print(f'nama: {self.nama} \nmotor: {self.motor} \narea: {self.area}')

class Gojek(Ojek): #inheritances
    
    def cek_id(self):
        print('Aplikasi Gojek') #dirubah, ditimpa, atau ditambahkan fungsi baru


ojek1=Ojek('Adhi','Honda','Jagakarsa')
ojek2=Gojek('Roman','Toyota','Ps. Kamis')

ojek1.cek_id()
ojek2.cek_id()