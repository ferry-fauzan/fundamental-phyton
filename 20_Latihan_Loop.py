
# print('*')
# print('**')
# print('***')
# print('****')

#latihan perulangan

# for
sisi=4

kali=1
# for i in range(sisi):
#     print('*'*kali)
#     kali+=1


# while
# while True:
#     kali+=1
#     print('*'*kali)

#     if kali == 5:
#         break

# count lewati * ganjil dan segitiga sama sisi
count=0
maks=10
space=int(maks/2)
while True:
    count+=1
    if count%2==1:
        continue

    print(' '*space,'+'*count)
    space-=1

    if count>maks:
        break 

# count=1
# while True:
#     if count%2:
#         print('*'*count)
#         count+=1
#     else:
#         count+=1
#         continue

#     if count>8:
#         break


