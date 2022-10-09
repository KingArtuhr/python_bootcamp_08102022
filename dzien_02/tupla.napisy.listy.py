#tuple
x = (1, 2, 3, "a", 4, 8, 2.0, "y")
print(x)
print(x[1])
print(len(x))
print(x[-2])
print(x[0:3])
print(x[::-1])

#napis
napis = "szedł sasza suchą szosą podczas suszy"
print(len(napis))
print(napis[1])
print(napis[-2])
print(napis[0:3])
print(napis[0::3])
print(napis[::-1])

#lista
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
lista.insert(2, 7)
print(lista)
print(lista[5])
lista[5] = 3
print(lista)
lista.append(7)
print(lista)
lista.pop(5)
print(lista)
lista.pop()
print(lista)
lista.remove(1)
print(lista)
lista.append(33)
print(lista)
lista.insert(2, "artur")
