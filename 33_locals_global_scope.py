#scope variabel local

kucing='muezza'

def rubahkucing(kucingbaru):
    kucing=kucingbaru
    print(f'Nama Kucing Baru saya {kucing}')
    
rubahkucing('maizza')
print(f'Nama kucing awals {kucing}')

#scope variabel global
kucing='nunu'

def rubahkucing(kucingbaru):
    global kucing
    kucing=kucingbaru
    print(f'Nama Kucing Baru saya 11 {kucing}')
    
rubahkucing('kinosa')
print(f'Nama kucing awal 11 {kucing}')