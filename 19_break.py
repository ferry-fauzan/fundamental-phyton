# break

nomor=2

# while nomor <6:
#     nomor+=1
#     print(f'Angka sekarang => {nomor}')


#     if nomor==5:
#         print('INI BREAK!!')
#         break

#     print('Mau Break')

# print('Finish')
masukkan_nomor=int(input('Masukkan nomor maksimal: '))
while True:
    nomor+=2
    print(f'Hitung angka {nomor}')

    if nomor==masukkan_nomor:
        print(f'Berhenti di angka: {masukkan_nomor}')
        break
print(f'Program Selesai')