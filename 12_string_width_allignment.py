data_nama='Ferry Fauzan'
data_umur='26'
data_tinggi='172 cm'
data_berat='58 kg'


#string standard
kenalin=f"Hai kenalin, gw {data_nama} umur gw {data_umur} gw ga tinggi amat si cuman {data_tinggi} "
print(5*'=','Data String',5*'=')
print(kenalin)


#string multiline
kenalin=f"Hai kenalin, gw {data_nama} \numur gw {data_umur} \ngw ga tinggi amat si cuman {data_tinggi} "
print(5*'=','Data String',5*'=')
print(kenalin)

#string multiline kutip 3
kenalin=f"""Hai kenalin, gw {data_nama}
umur gw {data_umur}
gw ga tinggi amat si cuman {data_tinggi}""" 
print(5*'=','Data String',5*'=')
print(kenalin)

#atur lebar
kenalin=f"""
Nama   = {data_nama:>15}
Umur   = {data_umur:<15}
Tinggi = {data_tinggi}""" 
print(5*'=','Data String',5*'=')
print(kenalin)

