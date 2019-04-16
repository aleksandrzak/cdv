def witaj():
    print('witaj Janusz!')
    pass
witaj()

def wyswietlWiek(wiek):
    print(f'Twój wiek: {wiek}')
    pass

wyswietlWiek(22)

def iloczyn(a, b):
    return a * b
    pass

print(iloczyn(3,4))

def iloraz(a, b):
    return a/b
    pass

iloraz1 = iloraz(3,4)
print(iloraz1)
print(type(iloraz1))

print(iloraz(b=5, a=2))


'''
uzytkownik podaje z klawiatury:
marka, model, pojemnosc, predkoscMax
utworz funkcje, ktora pobierze dane od uzytkownika i przypisze do slownika
utworz druga funkcje wyswietlajaca dane w formacie
Marka: ...
Model: ...
pojemnosc: ...
predkosc Maksymalna: ...
'''

marka = input('Podaj marke: ')
model = input('Podaj model: ')
pojemnosc = input('Podaj pojemnosc: ')
predkoscMax = input('Podaj predkosc maksymalną: ')

def funkcja2():
    print(f'Marka {marka} ')
    print(f'Model {model} ')
    print(f'Pojemnosc {pojemnosc} ')
    print(f'Marka {predkoscMax} ')

    pass


funkcja2()
