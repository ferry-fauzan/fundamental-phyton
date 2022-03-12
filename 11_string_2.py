#Lower & Upper

kabar="Luar Biasa Baik"
print("Normal: ", kabar)
kabar_upper=kabar.upper()
print("Upper is: ",kabar_upper)
kabar_lower=kabar.lower()
print("Lower is: " , kabar_lower)

#pengecekan lower&upper case
car="range rover sport"
car_low=car.islower()
print("Lowerkah?", car_low)
car_upper=car.isupper()
print("upperkah?", car_upper)

# isalpha() ,untuk cek huruf
# isalnum() ,untuk hurf dan angka
# isdecimal() ,untuk cek angka saja
# isspace() ,untuk cek spasi, tab, newline \n
#istitle() ,untuk cek semua katadimuali dengan huruf besar

judul= "Its Okay Not Gonna Be Okay"
cek_judul=judul.istitle()
print("Bener Awal Besar ?",cek_judul)

#ngecek awalan dengan kata tertentu
judul="Mini Cooper".startswith("Mini")

print("Judul awal sama?", judul)

# endswith("lorem") ,ngecek akhir kata

# penggabungan komponen join() dan split()
car=["rrs","mini cooper","hrv"]
print(car)

join=" mobil ".join(car)
print("Digabung nih: ", join)

print("mininya diilangin nih" ,join.split("mini"))

#alokasi karkater rjust(), ljust(), center()
car="rr evogue".rjust(5)
print("Dikananin nih: ",car)

car="mini cooper".center(19,"-")
print("Center nih: ",car)

#strip untuk mengembalikan alokasi karakter