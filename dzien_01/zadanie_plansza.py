x = int(input("Podaj liczbę: "))
y = int(input("Podaj liczbę: "))

if 0 <= x <= 10 and 0 <= y <= 10:
	print("jesteś w dolnej lewej części planszy")
elif 100 >= x >= 90 and 100 >= y >= 90:
	print("jesteś w górnej prawej części planszy")
elif 0 <= x <=10 and 10 < y < 90:
	print("jesteś w lewej centralnej części planszy")
elif 0 <= x <=10 and 100 >= y > 90:
	print("jesteś w górnej lewej części planszy")
elif 10 < x < 90 and 0 <= y <=10:
	print("jesteś w dolnej centralnej części tabeli")
elif  100 >= x > 90 and y <10:
    print("jesteś w dolnej prawej części planszy")
elif 10 < x < 90 and 10 < y < 90:
    print ("jesteś w centralnej części planszy")
elif 10 < x < 90 and 100 >= y > 90:
    print("jesteś w górnej centralnej częśći planszy")
elif 100 >= x > 90 and 10 < y < 90:
    print("jesteś w prawej centralnej części planszy")
else:
    print("jesteś poza planszą")
    
    