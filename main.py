#zadanie_1
#
# ulubione_sporty=['piłka nożna', 'koszykówka', 'aikido', 'pływanie']
# print(ulubione_sporty)
# ulubione_sporty.reverse()
# print(ulubione_sporty)
# ulubione_sporty.append('hokej')
# ulubione_sporty.append('tenis')
# ulubione_sporty.append('rugby')
# print(ulubione_sporty)

#zadanie_2

# skroty = {'str':'strona', 'nr':'numer', 'art':'artykuł', 'spr':'sprawdzić'}
# print(skroty)

#zadanie_3
# ulubione_gry = {'Saper':'9', 'Pasjans':'10', 'Zoo Tycoon':'10', 'The Great Giana Sisters':'7'}
# ## wartość to subiektywna ocena gry w skali 1-10
# print(ulubione_gry)
# print(len(ulubione_gry))

# #zadanie_4
# zdanie = input('Proszę napisać dowolne zdanie: ')
# print('Wpisane zdanie zawiera: ' + str(zdanie.count('a')) + ' liter(y) "a"')

# # zadanie_5
# import math
# a = input('Proszę podać wartość liczby całkowitej a: ')
# b = input('Teraz proszę podać wartość liczby całkowitej b: ')
# c = input('Na koniec poproszę o podanie wartości liczby całkowitej c: ')
# a, b, c = int(a), int(b), int(c)
# print(math.pow(a,b)+c)

# zadanie_6

# a = input('Proszę podać wartość liczby całkowitej a: ')
# b = input('Teraz proszę podać wartość liczby całkowitej b: ')
# c = input('Na koniec poproszę o podanie wartości liczby całkowitej c: ')
# a, b, c = int(a), int(b), int(c)
# if (a>b) & (a>c):
#     print('Liczba a jest największa')
# if (b>a) & (b>c):
#     print('Liczba b jest największa')
# if (c>a) & (c>b):
#     print('Liczba c jest największa')
#

# # zadanie_7
# import math
# liczby = [1, 1.5, 2, 2.5, 3, 3.5, 4]
# for x in range (len(liczby)):
#     liczby[x] = math.pow(liczby[x],2)
# print(liczby)

# zadanie_8
# liczby = []*10
# i = 0
# while i < 10:
#     liczby = (input('Wpisz liczbę: '))
#     i += 1
#
# for e in liczby:
#     if (e%2 == 0):
#         print('Oto liczby parzyste: ' + str(liczby))

# # zadanie_9
# import math
# a = float(input('Podaj liczbę nieujemną do obliczenia pierwiastka: '))
# try:
#     pierwiastek = pow(a, 0.5)
#     print('Obliczony pierwiastek wynosi: ' + str(pierwiastek))
# except ValueError:
#     print('Z tej liczby nie można obliczyć pierwiastka')