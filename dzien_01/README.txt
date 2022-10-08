# Podstawy

## Polecenia OS

- mkdir
- cd <nazwa>
- cd..


## Instalacja Pythona

- https://www.python.org/

## Ogólnie o językach programowania

### język maszynowy

### assemblery

mnemoniki - ADD

##Python

### przydatne funkcje na początku

- help
- dir

help()-interaktywna pomoc


help(print)
help(1)
help("str") - dokumentacja obiektu

dir() - wyświetlanie nazw z bieżącej przestrzeni
dir("napis") - zwraca liste atrybutów i metod danego obiektu



###Podstawowe typy

#### int - integer, liczby całkowite

Operacje: + - / * 
// - dzielenie całkowite
% - reszta z dzielenia - dzielenie modulo
** - potęgowanie pow(2,3)

##### system binarny

dwie cyfry = 1,0

0d = 0b
1d = 1b
2d = 10b = 1 * 2**1 + 0 * 2**0



0b11 - liczby przedstawione binarnie
0o11 - liczba ósemkowa
0x11 - liczba szesnastkowa

#### bool

wartości
False
True

operatory

and, or, not

operatory porównania:
== równe
>
<
>=
<=
!= różne

id()-adres w pamięci

####float - zmienno przecinkowa

#### complex

#### str - napis

dir("jakiś napis")

####

"%s == %d" % ("x", 10)
"{} == {}".format("x", 10)
"{a} == {b}".format (a="x", b=10)

najnowsza forma f"{a:30} == {b:5.2f}"

...
wiele 
linijek
...

"""
a
b
"""
f"""
{x}
"""


paragon:

nazwa waga cena
dla 3 produktów
+ wiersz podsumowania


#### zmienne (i stałe)
nazwy składają się z liter, cyfr i znaku podkreślenia, nie używamy polskich znaków (można), nie zaczynamy 
od cyfry

najlepiej pisać kod po angielsku

źle:
somevariable
someVariable
SomeVariable

dobrze:
some_variable

PEP8

for i in range(10):
	print(i)

napisz program który pobierze od użytkownika dane i wyliczy współczynnik BMI



### Wyrażenia warunkowe

if <warunek>:
	#ciało ifa
	print("wewnątrz ifa")
print("poza ifem")
	
	
	
if <warunek>:
	#ciało
	print("wew ifa")
else:
	print("wewnątrz else")
print ("poza ifem")


	
if <warunek>:
	#ciało
	print("wew ifa")
elif <warunek2>:
	print("wewnątrz elif")
print ("poza ifem")