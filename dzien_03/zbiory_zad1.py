"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych
przez użytkownika. Sprawdź jak dużo z tych liczb jest liczbami
parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
iloczynu.

"""

liczby_parzyste_od_0_do_100 = set(range(0, 101, 2))

liczby = set()

while True:
    liczba = input("podaj liczbę lub k by zakończyć: ")
    if liczba == "k":
        break
    liczba = int(liczba)
    liczby.add(liczba)

print(f"Unikalnych liczb: {len(liczby)}")
print(f"z czego parzystych od 0 do 100: {len(liczby & liczby_parzyste_od_0_do_100)}")

