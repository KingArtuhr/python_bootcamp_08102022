
wiersz = []
for i in range(10):
    wiersz = []
    for j in range(10):
        wiersz.append(i * j)
    wiersz.append(wiersz)

print(wiersz)
