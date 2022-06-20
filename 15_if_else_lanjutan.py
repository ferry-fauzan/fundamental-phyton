# Kalkulator sederhana
print(5*'=','KALKULATOR SEDERHANA',5*'=')
angka_1=int(input('Masukkan angka 1: '))
angka_2=int(input('Masukkan angka 2: '))
operator=input('Masukkan Operator: ')

if operator=='+':
    tambah=angka_1+angka_2
    print(f'Hasil: {tambah}')
elif operator=='-':
    kurang=angka_1-angka_2
    print(f'Hasil: {kurang}')
elif operator=='*':
    kali=angka_1*angka_2
    print(f'Hasil: {kali}')
elif operator=='/':
    bagi=angka_1/angka_2
    print(f'Hasil: {bagi}')
else:
    print('Operator belum terdaftar')


