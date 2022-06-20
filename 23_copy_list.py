name=['fauzan','ferry','chiko']
print(f'Nama kelas a: {hex(id(name))}')


nama_dup=name.copy() #duplicate list
print(f'Nama kelas b: {hex(id(nama_dup))}')
nama_dup[1]='otong'
print(f'Nama kelas b: {hex(id(nama_dup))}')