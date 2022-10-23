"""

zdefiniuj funkcję, która sprawdzi czy dana liczba jest liczbą pierwszą


"""

def czy_liczba_pierwsza(arg):
   for dzielnik in range(2, arg):
       if arg % dzielnik == 0:
        return False
   return True

assert czy_liczba_pierwsza(10) is False
assert czy_liczba_pierwsza(2) is True
assert czy_liczba_pierwsza(3) is True
assert czy_liczba_pierwsza(4) is False