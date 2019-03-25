print("CDV")
print(2)

#potęga
potega = 2 ** 10
print (potega)

tekst = "CDV"


print(tekst * 2)

#pobieranie danych z klawiatury
imie = input()
print("twoje imie podane z klawiatury: " + imie)

nazwisko = input()
print("twoje imie: " + imie + ", twoje nazwisko: " + nazwisko)


dlugosc = len(nazwisko)
print(type(nazwisko))
print(type(dlugosc))
print("dlugosc nazwiska: ", dlugosc)
dlugosc = str(dlugosc)	#konwersja danych int/str
print("dlugosc nazwiska: " + dlugosc)
print()

#uzytkownik wpisuje z klawiatury swoj wiek, wyswietl dane w formacie twoj wiek: ... lat

print("\nPodaj swoj wiek: ", end="")
wiek = input()
print("twoj wiek: ", wiek, " lat")

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

#ostatniZnak = nazwisko[len(nazwisko) - 1]
ostatniZnak = nazwisko[-1]

print(ostatniZnak)

#konwersja
x = "5"
print(type(x)) #str
x = int(x)
print(type(x)) #int

y = 4
print(type(y)) #int
y = y / 2
print(type(y)) #float
print(y) #2.0

wiek = 21
print("twoj wiek:", wiek)
wiek = str(wiek)
print("twoj wiek: " + wiek)

nazwisko = "Kowalski"
print(nazwisko[0]) #wyswietla 1 znak
print(nazwisko[0:3]) #kow
print(nazwisko[-2])	#k
print(nazwisko[-2:]) #ki
print(nazwisko[0:-2])	#kowals
print(nazwisko[:-2:2])	#kwl







