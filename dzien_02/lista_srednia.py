dane = []

while True:
    d = input("podaj liczbę lub k by zakończyć: ")

    if d == "k": break

    dane.append(int(d))
print(f"średnia ={sum(dane) / len(dane)}, min={min(dane)}, max={max(dane)} ")













