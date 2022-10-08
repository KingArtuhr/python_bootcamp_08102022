print("program do obliczania wskaźnika BMI")


Waga = float(input("podaj wagę w kg: "))
Wzrost = float(input ("podaj wzrost w cm: "))

bmi = Waga / (( Wzrost / 100 ) ** 2)

#print("Twój wskaźnik BMI wynosi:", round(bmi, 2))

print(f"Twój wskaźnik BMI wynosi {bmi:.2f}")