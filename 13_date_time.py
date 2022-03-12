#date n time

import datetime as dt
from re import A

print(5*'=','LIBRARY DATE',5*'=',)
tanggal=dt.date.today()
print(f"Today: {tanggal} \n")


print(5*'=','Masukkan Tanggal',5*'=')
print('Silahkan masukkan tanggal lahir anda \ntanggal, Bulan dan Tahun')

Tanggal=int(input('Tanggal \t:'))
Bulan=int(input('Bulan \t\t:'))
Tahun=int (input ('Tahun \t\t:'))

tanggal_lahir=dt.date(Tahun,Bulan,Tanggal)
print(18*'=+')
print('Anda Lahir pada Bulan: ',tanggal_lahir)
print(f"Hari lahir anda adalah: {tanggal_lahir:%A}")
print(18*'=+')

umur=tanggal-tanggal_lahir
umur_tahun=umur.days/365
print(f'Umur Kamu: {umur_tahun} tahun')