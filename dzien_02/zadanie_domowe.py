wiersz = []
for i in range(10):
    print(i)
    wiersz = [i + 1]
    for j in range(10):
        wiersz.append(i * j)
        wiersz.append(wiersz)

print(wiersz)