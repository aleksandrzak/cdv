programowanie = ['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print(pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatniElement = programowanie[-1]
print(ostatniElement)

# dodanie nowego elementu do listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

# zkiczanie elementów w liscie
ile = programowanie.count('Python')
print(ile)

# ilość elementów w liscie
iloscElementow = len(programowanie)
print(iloscElementow)

# połączenie listy
inneJezyki = ['C', 'C++']
programowanie.extend(inneJezyki)
print(programowanie)

# czyszczenie listy
nowa = programowanie
print('Lista nowa:', end="")
print(nowa)
nowa.clear()
print('Lista nowa:', end="")
print(nowa)
print(programowanie)
