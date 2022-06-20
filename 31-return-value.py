#fungsi dengan return value
def kuadrat(argumen):
    total= argumen**2
    print(f'nilai kuadrat dari {argumen} adalah {total}')
    return(total)

a=kuadrat(3)
print(a)

#fungsi dengan return value dan multiple argumen 
def tambah(tambah1,tambah2):
    total=tambah1+tambah2
    print(f'{tambah1} + {tambah2} = {total}')
    return total

b=tambah(1,kuadrat(2))
print(b)

