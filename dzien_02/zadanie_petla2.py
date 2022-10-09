
suma_liczb = 0
ilosc_zapytan = 0

max_nr = None
min_nr = None

while True:
    dane = input("podaj liczbę (lub k by zakończyć): ")

    if dane == "k":
        break
    dane = int(dane)
    suma_liczb = suma_liczb + dane
    ilosc_zapytan += 1

    if max_nr is None or dane > max_nr:
        max_nr = dane

    if min_nr is None or dane < min_nr:
        min_nr = dane

print("średnia wynosi", suma_liczb / ilosc_zapytan)
print("max: ", max_nr)
print("min: ", min_nr)