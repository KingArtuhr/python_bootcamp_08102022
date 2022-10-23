# definiowanie funkcji

def nazwa_funkcji():
    print("coś sobie robię...")



nazwa_funkcji()
nazwa_funkcji()
nazwa_funkcji()

def funkcja_z_1_arg(arg):
    print("coś sobie robię z...", arg)


funkcja_z_1_arg(11)

def suma_3_liczb(a: int, b: int, c: int) -> int:
    return a + b + c

w = suma_3_liczb(56, 25, 89)
print(w)
suma_3_liczb('a', 'b', 'c')

#definiowani ewartości domyślniej dla parametru

def increment(value: int, step: int = 1) -> int:
    return value + step

print(increment(5,2))
print(increment(5))
