
ceny = {'marchew' : 3,'ziemniaki' : 2,'pomidory' : 12}
magazyn = {'marchew' : 5,'ziemniaki' : 5,'pomidory' : 5}

print('witaj w warzywniaku, dzisiaj oferujemy: ')

tryb = input("Rodzaj pracy: m-magazyn, k-kasa, z-zakończ")

if tryb == k:

    for produkt, cena in ceny.items():
        print(f' - {produkt:30} : {cena:5.2f} PLN\kg')


    koszt = 0

    while True:
        produkt = input("co chcesz kupić? (Enter by zakończyć)")
        if produkt == "":
            break
        waga =float(input(f' ile chcesz kupić? ({produkt}): '))

        if waga > magazyn[produkt]:
            print(f"przepraszam mam tylko {magazyn[produkt]} kg {produkt}")
        else:
            koszt += waga * ceny[produkt]


    if koszt:
        print (f"należy się: {koszt:.2f} PLN")
    else:
        print("może inym razem")

else:
    print("Dziękujemy! Zapraszamy ponownie!")


