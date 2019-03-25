tekst = "Anna, paweł, TomEK"

tab = tekst.split(", ")
print(tekst)
print(tab)
print(type(tab))	#list

imie1 = tab[0]
print(imie1)	#Anna

print("Twoje imie: " + imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

#sprawdzenie zawartosci
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)
print(type(zawartosc))

nazwisko = ""
print(nazwisko.isalpha())	#false

imie = "Julia"
print("\nDane uzytkownika\nMasz na imie:", imie)

tekst1 = "Jan\n"
tekst2 = "Nowak"
print(tekst1 + tekst2)

tekst1 = tekst1.rstrip()
print(tekst1 + tekst2)
print(tekst1 + " " + tekst2)

#wyswietlanie lancuchow znakow

#wszystkie zmienne Pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje Pythona 2.6 +
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "marzec"
dzien = 25

print("Data: ", end="")
print(dzien, miesiac, rok)

print("Data: ", end="")
print(dzien, miesiac, rok, sep="-")










print()
