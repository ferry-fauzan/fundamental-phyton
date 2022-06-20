
data=['fauzan', 'ferry', 'sakola']
data_awal=data[0]
print(data_awal)

panjang=len(data)
print(panjang)

#manipulasi data list
data.insert(1,'Fahri') #nambah data awal
print(f'Data new {data}')

data.append('Nurjaman') #nambah data akhir
print(f'Data new {data}')

data_new=['seiko','yahiko']
data.extend(data_new) #gabungkan data
print(f'Data New {data}')

data[3]='Rasicha' #ganti isi string
print(data)

data.remove('sakola')
print(data)