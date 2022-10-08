produkt_1 = 'pomidory'
waga_1 = 10
cena_1 = 12.5

produkt_2 = 'ogórki'
waga_2 = 5
cena_2 = 3.7

produkt_3 = 'ser gouda'
waga_3 = 0.8
cena_3 = 17

raport = f"""
{"produkt":15} {"waga":13} {"cena"}

{produkt_1:15} {waga_1:5.2f} kg {cena_1:10.2f} PLN
{produkt_2:15} {waga_2:5.2f} kg {cena_2:10.2f} PLN
{produkt_3:15} {waga_3:5.2f} kg {cena_3:10.2f} PLN
{"-"*50}
{"suma:":15} {waga_1+waga_2+waga_3:5.2f} kg {cena_1+cena_2+cena_3:10.2f} PLN
"""

print(raport)

