quote = 'A good programmer is someone who always looks both ways before crossing one-way street'
print(quote.upper()) # zmiana na duże litery
print(quote.lower()) # zmiana na małe litery
print(quote.endswith('street')) # sprawdza czy zdanie kończy się słowem street
print(quote.isupper()) # sprawdza czy teskt napisany jest dużymi literami
print(quote.upper().isupper()) # sprawdza czy po zmianie na duże litery napis jest dużymi literami
print(quote.find('one')) #wyszukuje w tekście pierwszej litery szukanego słowa
print(quote.replace('one', '1')) # zamienia słowo "one" na "1"
print(quote.replace('one', '1').replace('both', '2'))
print(quote.split(' ')) # rozdzielenie napisu ze względu na spację, zwraca nam listę
print(quote.isdigit()) # sprawdza czy napis jest liczbą
print(quote.isdecimal()) # spraqwdza czy napis jest liczbą dziesiętną
print(quote.isalpha()) # sprawdza czy napis jest napisem bez liczb
print(quote.isalnum()) #sprawdza czy nap[is jest napisem z literami i cyframi






