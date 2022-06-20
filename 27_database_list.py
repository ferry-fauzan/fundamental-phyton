#program list buku


list_buku=[]
while True:
    judul=input(f'Judul Buku:\t')
    penulis=input(f'Nama Penulis:\t')
    
    data_buku=[judul,penulis]
    list_buku.append(data_buku)    
    # print(list_buku)
    for index,data in enumerate(list_buku):
        print(f'{index+1} | Judul Buku: {data[0]} | Penulis: {data[1]}')
    
    lanjut=input(f'Apakah Lanjut? (y/n)')

    if lanjut=='n':
        break
print('PROGRAM SELESAI')
