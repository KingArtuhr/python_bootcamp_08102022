# licznik liter

zadany_text = "ala ma kota"

#napisz skrypt który utworzy słownik zawierający liczbę wystąpień danego znaku
#w zadanym tekscie
i=1
slownik = {}
for litera in zadany_text:
    if litera in slownik:
        slownik[litera] +=1
    else:
        slownik[litera] = 1
    i += 1
print(slownik)
print(i)

i=1
slownik = {}
for litera in zadany_text:
    slownik[litera] = slownik.get(litera, 0) + 1
    i += 1
print(slownik)
print(i)

i=1
zliczenia = {}
for znak in zadany_text:
    zliczenia[znak] = zadany_text.count(znak)
    i += 1
print(zliczenia)
print(i)

