#if else cuy

from tkinter.simpledialog import askstring


password=input('Paswordnya apa nih: ')
print(password)

# if kondisi:aksi 
# program selanjutnya

if password=='kopi enak': print('Wellcome to the jungle')
print(f'yak betul {password} ')


#program if indentation
if password=='kopi enak':
    print('Kopi Luwak')
    print('Beli yaa')
print(f'Terima Kasih porgram selesai')

#else condition
if password=='kopi enak':
    print('Password betul')
else:
    print('Password anda salah')

print('Akhir Program')