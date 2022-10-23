# przypomnienie

list = [1, 2, 3, 'a']
tupla = (1, 2, 3, 4)

print(tupla[2])

#słowniki

pusty_slownik = {}
pusty_slownik_2 = dict()

#dodawanie wartości

litery ={}
litery["a"] = 1
print(litery)

litery = { 'a': 1, 'b': 2}

print(litery['b'])

#litery id b - czasami tak się mówi

litery['b'] = litery['b'] + 1
litery ['b'] += 1

print(litery['b'])

####################

litery['c'] = 0
litery['c'] += 1
print(litery)

print(dir(litery))
print("keys", litery.keys())
print("values", litery.values())
print("items", litery.items())

#czy wszystko może być wartością i kluczem?
#wartości tak, dowolne
#klucze - obiekty hashowalne -  z dużym przybliżeniem możemy uznać że chodzi o obiekty niehasowalne
#hash - "unikalna", stała reprezentacja - wylicznana na podstawie zawartosci
#klucze - unikalne, hashowalne

d = {(1, 2): 'abcde'}
print(d)

for k, v in litery.items():
    print(v, k)


print(litery.items())

#tworzenie
s = {}
s = {1: "a", 2: "b"}

#pobieranie
S[1]
#modyfikacja
s[1] = "c"

#usuwanie
#s.pop(1)

del s[1]
print(s)
