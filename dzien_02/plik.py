x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

szesciany = []
for el in x:
    szesciany.append(el ** 3)

szesciany2 = [el ** 3 for el in x]

szesciany_liczb_parzystych = []
for el in x:
    if x % 2 == 0:
        szesciany.append(el ** 3)

szesciany_liczb_parzystych2= [el ** 3 for el in x if el % 2 == 0]