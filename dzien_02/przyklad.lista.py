print(dir([]))

lista = [1,2,3,4,5,6]

print(lista)

print(lista.count(2))

#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

lista.append(4)

print(lista)

dane = [ 1, 1, 2, 2, 1, 2.0, 1.0]
#print()
#i = 1
#while i < len(dane):
#    print(dane[i])
#    i +=1

szukane = 2
licznik_wyszukania = 0
for el in dane:
    if el == szukane:
        licznik_wyszukania += 1
print(el)
