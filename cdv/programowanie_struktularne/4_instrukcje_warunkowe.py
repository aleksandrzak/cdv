x = 6
if x==5:
    print('x jest równe 5')
    print('x jest równe 5')
    print('x jest równe 5')
else:
    print('x nie jest równe 5')
    print('x wynosi', x)

###########################
y = True    #False
if y:
    print('prawda')
else:
    print('fałsz')

#########################

z = 5 > 6
if z:
    print('prawda')
else:
    print('fałsz')

############

# j = '1'
# j = '0'
# j = ''
j = False
if bool(j):
    print('1')
else:
    print('0')

k = input('Podaj k: ')
if bool(k):
    print('zmienna k zawiera dane')
else:
    print('zmienna k nie zawiera danych')
