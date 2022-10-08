miasto_a = input("miasto A: ")
miasto_b = input("miasto B: ")

dystans = int(input(f"odległość pomiędzy {miasto_a}-{miasto_b}: "))

cena_paliwa = float(input("Cena paliwa: "))

spalanie = float (input("spalanie na 100 km: ")) 

koszt = (dystans/100)*spalanie*cena_paliwa

print("Koszt przejazdu z", miasto_a, "do", miasto_b, "wynosi", round(koszt,2))


