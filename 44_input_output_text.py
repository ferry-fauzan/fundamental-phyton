#input output file
#membuat file text
"""
w=write mode/mode menulis dan menghapus file nama, jika tidak ada maka akan dibuatkan file baru
r=read mode only'hanya bisa baca
a=appending mode/menambahkan data diakhir baris
r+ = write and read mode
"""

file=open("data.txt",'w')

file.write('Ini dbuat dengan text phyton')
file.write("\nIni dibaris kedua")
file.close()

#membaca file text
file2=open('data.txt','r')

# print(file2.read())

print(file2.readline())

file2.close()


#appending mode

file3=open('data.txt','a')
file3.write('\nbaris ini dibuat dengan mode append')

file3.close

