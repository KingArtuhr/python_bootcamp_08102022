x = float(input("podaj pierwszą liczbę: "))
y = float(input("podaj drugą liczbę: "))
z = input("podaj rodzaj działania: ")

if z == "+":
	print(x + y)
elif z == "-":
	print(x - y)
elif z == "*":
	print (x * y)
elif z == "/":
    if y == 0:
        print("Pamiętaj cholero nie dziel przez zero")
    else:
        print(x / y)
elif z == "^":
	print( x ** y)
else:
    print("nie znana operacja") 
	
