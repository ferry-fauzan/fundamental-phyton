def jumlah(a,b):
    c=a+b
    return c

hasil=jumlah(4,5)
#membuat anonymous lambda function
#kali=lambda argumen: print(argumen)

kali=lambda x,y: x*y
hasil=kali(4,5)
print(kali(3,5))
print(hasil)