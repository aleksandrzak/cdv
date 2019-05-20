#pętle zadania

'''
    podaj wartosc poczatkowa i koncowa, ktora bedzie wypisana w porzadku malejacym
    uzytkownik podaje x i y i posortowac w porzadku nie rosnacym
'''
'''
x = int(input('podaj x: '))
y = int(input('podaj y: ')) -1

if y > x:
    pom = x
    x = y + 1
    y = pom -1


for i in range(x, y, -1):
    print(f'{i}',end=' ')
    pass
print()
'''



for i in range(1,6):
    for j in range(1,i+1):
        print('*', end='')
        pass
    print()
    pass
print()


'''
i = 1
ilosc = int(input('podaj ilosc wierszy: '))+1
znak = input('podaj znak do wyswietlenia: ')
print()

for i in range(1,ilosc):
    print(znak * i)
    i = i + 1
    pass
print()
'''

#########################################
'''
a = float(input('podaj a: '))
b = float(input('podaj b: '))

wynik = 0.0
dol = a*a+2*a*b+b*b


if dol == 0:
    print("nie dzielimy przez 0")
else:
    wynik = ((a*a+b)/(dol))
    print(wynik)
'''

################################

school = 'CDV Poznan'

for letter in school:
    if letter == 'V' or letter == ' ':
        continue
    print(f'litera:{letter}')
print()


#############
'''
x = 10

while x > 0:
    x = x - 1
    if x == 6:
        continue
    print(f'{x}',end=' ')
print('Koniec programu!')
'''

'''
uzytkownik podaje z klawiatury haslo
jesli poda haslo 'okon' to na ekranie wyswietli
sie komunikat 'poprawne haslo'
uzytkownik ma na podanie 3 proby
jesli przekroczy to wywali error 'przekroczono limit prob'

'''
import os
os.system('cls')

x = 3
p=0
while x > 0:
    x = x - 1
    p=p+1
    haslo = input('podaj haslo: ')
    if haslo == 'okon':
        os.system('cls')
        print('podales dobre haslo')
        print(f'potrzebowales na to {p} prob')
        break
    if x == 0:
        os.system('cls')
        print('wykorzystales wszystkie proby')


'''
zadanie dodatkowe
obliczyc
a^2 + b dla c > 0
a - b^2 dla c < 0
1/(a-b) dla c = 0
przyklad a=4 b=5 c=1 wynik=21
        a=10 b=10 c=0 wynik=proba dzielenia przez 0
'''







###
