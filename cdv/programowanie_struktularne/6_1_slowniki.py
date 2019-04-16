slowniki = {'klucz1':'wartosc1', 'klucz2': 'wartosc2'}

'''
    utworz slowniki o nazwie pracownik zawierajacy klucze:
    imie, nazwisko, miasto, wiek, imionaDzieci, imionaRodzicow
'''

pracownik = {
    'imie':"Janusz",
    'nazwisko':"Nosacz",
    'miasto':"Poznan",
    'wiek':69,
    'imionaDzieci':['Anna', 'Tomasz'],
    'imionaRodzicow':['Julia', 'Paweł']
}

print(pracownik)
print(pracownik['imionaDzieci'])
print(pracownik['imionaDzieci'][0])

pracownik['wzrost'] = 175
pracownik['waga'] = 75
print(pracownik)

#####################################

pracownik1 = {
    'imie':"Janusz",
    'nazwisko':"Nosacz",
    'miasto':"Poznan",
    'wiek':69,
}

print()
print(pracownik1)

klucz = 'wiek'
if klucz in pracownik1:
    del pracownik1[klucz]
    print(f'Klucz {klucz} zostal usuniety')
else:
    print(f'Klucz {klucz} nie zostal usuniety')

print(pracownik1)
print(pracownik1.keys())
print(pracownik1.values())
print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=' ')

print()

for key, value in pracownik1.items():
    print(f'{key}: {value}')
