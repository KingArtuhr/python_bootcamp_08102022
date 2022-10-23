lista = [9, 1, 6, 8, 4, 3, 2, 0]
print(lista)

def sortowanie_przez_wybieranie(lista):
    for i_podstawienia in range(len(lista)):
        print(i_podstawienia)
        i_min_wartosci = i_podstawienia
        for i_ogona in range(i_podstawienia+1, len(lista)):
            if lista[i_ogona] < lista[i_min_wartosci]:
                i_min_wartosci = i_ogona

        #temp = lista[i_min_wartosci]
        #lista[i_min_wartosci] = lista[i_podtsawienia]
        #lista[i_podstawienia] = temp

        lista[i_min_wartosci], lista[i_podstawienia] = lista[i_podstawienia], lista [i_min_wartosci]
    return lista


print(lista)
assert lista == [0, 1, 2, 3, 4, 6, 8, 9]
