imiona = ['Julia', 'Anna', 'Krystyna']
print(type(imiona)) # <class 'list'>
imiona.append('Janusz')
ilosc = len(imiona)
print(f'ilosc imion:  {ilosc}')


# tuple
nazwiska = ('Kowalski', 'Nowak')
print(type(nazwiska)) # <class 'tuple'>
print(nazwiska)

# slowniki
osoba = {
    'imie':"Julia",
    'nazwisko': "Nowak",
    'wiek':23
}
print(osoba)
print(type(osoba)) # <class 'dict>
print(osoba['nazwisko'])
print(osoba.keys()) # dict_keys(['imie', 'nazwisko', 'wiek'])
print(osoba.get('wzrost','brak danych'))
print(osoba.get('imie','brak danych'))
