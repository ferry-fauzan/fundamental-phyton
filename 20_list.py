#cara alternatif buat list
oi=range(1,11,2)
listi=list(oi)
print(listi)

#list comprehension
list_for=[i**2 for i in range(0,11)]
print(list_for)

#list dengan for dan if
list_for_if=[i for i in range(1,8) if i!=5]
print(list_for_if)