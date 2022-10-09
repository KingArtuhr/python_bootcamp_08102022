import random

DEBUG = True
DIM_X = 10
DIM_Y = 10

gracz_x = random.randint(1, DIM_X)
gracz_y = random.randint(1, DIM_Y)

skarb_x = random.randint(1, DIM_X)
skarb_y = random.randint(1, DIM_Y)

ruch_counter = 0

odleglosc_poczatkowa = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

while True:

    print(f"pozycja graca: {gracz_x=} {gracz_y=}")

    odleglosc_przed = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    polecenie = input("wykonaj ruch (w-góra, a-lewo, s-dół, d-prawo): ")
    if polecenie in "wsad" and len(polecenie) == 1:
        ruch_counter += 1

    if polecenie == "w":
        gracz_y += 1
    elif polecenie == "s":
        gracz_y -= 1
    elif polecenie == "a":
        gracz_x -= 1
    elif polecenie == "d":
        gracz_x += 1
    else:
        print("Nie o co Ci chodzi")

    if gracz_y == skarb_y and gracz_x == skarb_x:
        print(f"znalazłeś skarb!!! w {ruch_counter} ruchach")
        break

    if gracz_y > 10 or gracz_x > 10 or gracz_y < 0 or gracz_x < 0:
        print("wypadłeś poza planszę")
        break

    if ruch_counter > 2 * odleglosc_poczatkowa:
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        ruch_counter = 0
        odleglosc_poczatkowa = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        print("za długo blądzisz - skarb zmienił położenie")
        continue

    odleglosc_po = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    if random.randint(1, 5) != 2:
        if odleglosc_po < odleglosc_przed:
            print("ciepło")
        elif odleglosc_po > odleglosc_przed:
            print("zimno")
    else:
        print(" A nie powiem !!!")

    if DEBUG:
        print(f"pozycja skarbu: {skarb_x=} {skarb_y=}")
