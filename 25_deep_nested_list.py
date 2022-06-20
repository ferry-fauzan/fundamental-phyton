data1=[1,3,4,5]
data2=[5,6,3,44]

unidata=[data1,data2]

#ambil data dalam list
data=unidata[1][3]
print(f'Data: {data}')

#deep copy
from copy import deepcopy
unidata=[data1,data2,10]
data_dcpy=deepcopy(unidata)

print(f'Address asli: {hex(id(unidata))}')
print(f'Address asli: {hex(id(data_dcpy))}')

print(f'Address asli: {unidata}')
print(f'Address asli: {data_dcpy}')

